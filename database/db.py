from flask_mongoengine import MongoEngine

db = MongoEngine()

def inicializa_db(app):
    db.init_app(app)