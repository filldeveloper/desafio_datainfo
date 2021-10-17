from .db import db

class News(db.Document):
    titulo = db.StringField(required=True)
    noticia = db.StringField(required=True)
    autor = db.StringField(required=True)