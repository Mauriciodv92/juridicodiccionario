from flask import Blueprint, render_template, redirect, url_for, request, session, flash, current_app
from models.termino import TerminoModel
from utils.auth import validar_usuario
from utils.file import save_file

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        pwd = request.form['clave']
        if validar_usuario(user, pwd):
            session['admin'] = user
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Credenciales inválidas')
    return render_template('admin/login.html')


@admin.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)

    return decorated_function


@admin.route('/')
@login_required
def dashboard():
    terminos = TerminoModel.obtener_todos()
    return render_template('admin/dashboard.html', terminos=terminos)


# ...
@admin.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre_imagen = save_file(request.files.get('imagen'), current_app.config['ALLOWED_IMAGE_EXTENSIONS'])
        nombre_video = save_file(request.files.get('video'), current_app.config['ALLOWED_VIDEO_EXTENSIONS'])
        termino = {
            "termino": request.form['termino'],
            "descripcion": request.form['descripcion'],
            "imagen": nombre_imagen,
            "video": nombre_video
        }
        TerminoModel.insertar_termino(termino)
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/nuevo.html')


@admin.route('/editar/<id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    termino = TerminoModel.obtener_por_id(id)
    if request.method == 'POST':
        nombre_imagen = save_file(request.files.get('imagen'), current_app.config['ALLOWED_IMAGE_EXTENSIONS'])
        nombre_video = save_file(request.files.get('video'), current_app.config['ALLOWED_VIDEO_EXTENSIONS'])
        datos = {
            "termino": request.form['termino'],
            "descripcion": request.form['descripcion']
        }
        # Solo actualiza si hay archivos nuevos
        if nombre_imagen:
            datos["imagen"] = nombre_imagen
        if nombre_video:
            datos["video"] = nombre_video
        TerminoModel.actualizar_termino(id, datos)
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/editar.html', termino=termino)


@admin.route('/eliminar/<id>', methods=['GET', 'POST'])
@login_required
def eliminar(id):
    if request.method == 'POST':
        TerminoModel.eliminar_termino(id)
        return redirect(url_for('admin.dashboard'))
    termino = TerminoModel.obtener_por_id(id)
    return render_template('admin/eliminar.html', termino=termino)
