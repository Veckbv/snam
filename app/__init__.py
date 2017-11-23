from flask import Flask 
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__, instance_path='/home/ali/myapps/snam/manga')
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)    

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app