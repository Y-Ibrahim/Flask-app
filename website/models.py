from . import db
from sqlalchemy.sql import func


class Image(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        image_type = db.Column(db.String(100), nullable=False)
        image_url = db.Column(db.String(100), nullable=False)
        image_title = db.Column(db.String(100), nullable=False)
        image_text = db.Column(db.String(100), nullable=False)