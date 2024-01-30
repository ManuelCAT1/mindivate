





from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer



db = SQLAlchemy()
DB_NAME = "Mindivatedatabase.db"
mail = Mail()  # Initialize mail

def create_app(environ=None, start_response=None):
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    




    app.config['SECRET_KEY'] = 'MindivateNewSuperNewKey'
    app.config['SECURITY_PASSWORD_SALT'] = 'AnotherSupergoodMindivateNewSuperNewKey'
    


    app.config['MAIL_SERVER'] = 'serwer2416771.home.pl'
 
    app.config['MAIL_PORT'] = 587
  
    app.config['MAIL_USE_TLS'] = True  # Enable TLS
    
    app.config['MAIL_USE_SSL'] = False  # Keep SSL disabled
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'email@mindivate.com')

    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'futwam-dejzix-paxqA0')
 
    app.config['MAIL_DEFAULT_SENDER'] = 'email@mindivate.com'
 
    db.init_app(app)

    mail.init_app(app)  # Initialize mail with the app



    

    with app.app_context():
        db.create_all()



    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

   

    login_manager = LoginManager()
    login_manager.login_view = 'auth.loginPage'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    from . import models

    with app.app_context():
        db.create_all()


    return app