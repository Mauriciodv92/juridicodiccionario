import os
from werkzeug.utils import secure_filename
from flask import current_app

def allowed_file(filename, allowed_set):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set

def save_file(file_storage, allowed_set):
    if file_storage and allowed_file(file_storage.filename, allowed_set):
        filename = secure_filename(file_storage.filename)
        path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file_storage.save(path)
        return filename
    return None
