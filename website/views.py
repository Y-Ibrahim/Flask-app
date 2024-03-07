from flask import Blueprint, render_template
from .models import Image
views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template('home.html')

@views.route('/gallery', methods=['GET', 'POST'])
def gallery():
    imageCards = Image.query.all()
    return render_template('gallery.html', imageCards=imageCards)
