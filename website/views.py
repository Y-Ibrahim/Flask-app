from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db 
from .models import Image
views = Blueprint("views", __name__)
from sqlalchemy.exc import OperationalError, IntegrityError

@views.route("/")
def home():
    return render_template('home.html')

@views.route('/gallery', methods=['GET', 'POST'])
def gallery():
    try:
        imageCards = Image.query.all()
        # post 'New Post' form data to table
        if request.method == 'POST':
       
            # Get form data
            imageType = request.form.get("imageType")
            image = request.form.get("image")
            imageTitle = request.form.get('imageTitle')
            imageText = request.form.get('imageText')
            print(imageType)
            # check if post already exists
            

            # Insert data into MySQL database
            newPost = Image(image_type=imageType, image_url=image, image_title=imageTitle, image_text=imageText)
            db.session.add(newPost)
            db.session.commit()
            flash("New Post Created")
            return redirect(url_for('views.gallery'))
        else: 
            return render_template('gallery.html', imageCards=imageCards)

    except OperationalError as e:
        # set db_error to true
        dbError = True
        return render_template('gallery.html', dbError=dbError)
        
