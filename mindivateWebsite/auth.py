from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login  import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)




@auth.route('/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if password == user.password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.email'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')

    # This return statement will handle GET requests and POST requests that don't result in a redirect.
    return render_template("login.html")


        





# @auth.route('/register', methods=['GET', 'POST'])
# def registerPage():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         password2 = request.form.get('password2')

#         user_email = User.query.filter_by(email=email).first()
#         user_username = User.query.filter_by(username=username).first()

#         if user_email:
#             flash('Email already exists.', category='error')
#         elif user_username:
#             flash('Username already exists.', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 3 characters.', category='error')
#         elif len(username) < 2:
#             flash('Username must be greater than 1 character.', category='error')
#         elif password != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
#             new_user = User(email=email, username=username, password=password)
#             db.session.add(new_user)
#             db.session.commit()
            
#             flash('Account created!', category='success')
#             return redirect(url_for('auth.loginPage'))

#     return render_template("register.html")





@auth.route('/logout')
@login_required
def logoutPage():
    logout_user()
    return redirect(url_for('auth.loginPage'))




@auth.errorhandler(401)
def unauthorized_error(error):
    return redirect(url_for('auth.loginPage')), 401
