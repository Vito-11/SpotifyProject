from flask import *
from flask_login import login_required, current_user
from . import db
from . import __init__
from .models import User  # importing User class from models.py
from . import db  # importing db object from __init__.py
from datetime import datetime
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename


main = Blueprint('main', __name__)

@main.route('/') #the route function tells the application which url should call associated function
def index():
    return render_template('index.html')

@main.route('/signup')
@login_required
def signup():
    return render_template('signup.html')

@main.route('/login')
def login():
    return render_template('login1.html')

@main.route('/search')
def search():
    return render_template('search.html')

@main.route('/foryourlisting')
def foryourlisting():
    return render_template('foryourlisting.html')

@main.route('/chart')
def chart():
    return render_template('chart.html')

@main.route('/artist')
def artist():
    return render_template('artist.html')


@main.route('/profile')
@login_required
def profile():
    #image_file=url_for('static',filename='profile_pics/'+current_user.image_file)     # ,image_file=image_file
    return render_template('profile.html', name=current_user.name, email=current_user.email, gender=current_user.gender, dob=current_user.dob)


@main.route('/update')
@login_required
def update():                                                                     #, image_file = current_user.image_file)
	return render_template('update.html', name=current_user.name, email=current_user.email, gender=current_user.gender, dob=current_user.dob)


@main.route('/edit', methods=["POST"])
@login_required
def edit():
    name=request.form['name']
    email = request.form['email']
    dob = request.form['dob']
    y,m,d=dob.split('-')
    dob = datetime(int(y), int(m), int(d))
    gender = request.form['gender']
    #image_file=request.files['file']


    edit_user = User.query.filter_by(id=current_user.id).first_or_404()
    edit_user.email=email
    edit_user.name=name
    edit_user.dob = dob
    edit_user.gender = gender
    #edit_user.image_file=image_file
  
    db.session.commit()
    flash("Details updated successfully")
    return redirect(url_for('main.profile'))

@main.route('/base')
def base():
	return render_template('base.html')

@main.route('/playlist')
def playlist():
	return render_template('playlist.html')	    


#onClick = "window.location.href='{{ url_for('main.profile') }}' ;"

#@main.route('/upload')
#def upload_file():
 #  return render_template('base.html')


