import unittest
from app import create_app
from models.termino import mongo
from utils.auth import validar_usuario

# =======================
# Prueba 1: Inicio de la aplicación
# =======================
class TestAppInitialization(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        mongo.cx.close()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# =======================
# Prueba 2: Insertar y recuperar término
# =======================
class TestTerminoModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        mongo.db.terminos.delete_many({})

    def tearDown(self):
        mongo.db.terminos.delete_many({})
        self.app_context.pop()
        mongo.cx.close()

    def test_insertar_y_obtener_termino(self):
        termino = {
            "termino": "Test",
            "descripcion": "Esto es un término de prueba",
            "imagen": None,
            "video": None
        }
        mongo.db.terminos.insert_one(termino)
        resultado = mongo.db.terminos.find_one({"termino": "Test"})
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado['descripcion'], "Esto es un término de prueba")

# =======================
# Prueba 3: Verificar autenticación falsa
# =======================
class TestAuth(unittest.TestCase):
    def test_validar_usuario_invalido(self):
        self.assertFalse(validar_usuario("usuario_falso", "clave_incorrecta"))

# =======================
# Prueba 4: Buscar término existente
# =======================
class TestBuscarTermino(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        mongo.db.terminos.delete_many({})
        mongo.db.terminos.insert_one({
            "termino": "Tutela",
            "descripcion": "Protección de derechos fundamentales"
        })

    def tearDown(self):
        mongo.db.terminos.delete_many({})
        self.app_context.pop()
        mongo.cx.close()

    def test_buscar_termino(self):
        resultados = list(mongo.db.terminos.find({"termino": {"$regex": "tutela", "$options": "i"}}))
        self.assertTrue(len(resultados) > 0)
        self.assertEqual(resultados[0]['termino'], "Tutela")

# =======================
# Prueba 5: Eliminar término
# =======================
class TestEliminarTermino(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        mongo.db.terminos.delete_many({})

    def tearDown(self):
        mongo.db.terminos.delete_many({})
        self.app_context.pop()
        mongo.cx.close()

    def test_eliminar_termino(self):
        id_insertado = mongo.db.terminos.insert_one({
            "termino": "Eliminar",
            "descripcion": "Término de prueba para eliminar"
        }).inserted_id

        mongo.db.terminos.delete_one({"_id": id_insertado})
        eliminado = mongo.db.terminos.find_one({"_id": id_insertado})
        self.assertIsNone(eliminado)

# =======================
# Prueba 6: Redirección al login sin sesión
# =======================
class TestRedireccionSinSesion(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        mongo.cx.close()

    def test_redireccion_login(self):
        response = self.client.get("/admin/", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login", response.headers["Location"])

# =======================
# Prueba 7: Página de login carga
# =======================
class TestLoginCarga(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        mongo.cx.close()

    def test_login_status_code(self):
        response = self.client.get("/admin/login")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
