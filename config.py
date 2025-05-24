import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/diccionariojuridico")
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_here'
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads')
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'webm', 'ogg'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

