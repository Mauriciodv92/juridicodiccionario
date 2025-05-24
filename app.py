from flask import Flask
from config import Config
from models.termino import mongo
from controllers.admin_controller import admin
from controllers.client_controller import client


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)

    app.register_blueprint(admin)
    app.register_blueprint(client)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
