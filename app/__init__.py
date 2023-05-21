from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] =
app.config.from_object('config.Config')
# images_folder = os.path.join('static', 'images')
# , static_url_path='/static'
# app.config['UPLOAD_FOLDER'] = images_folder

db = SQLAlchemy(app)
from .views import *
from .models import *

app.app_context().push()
db.create_all()

manager = LoginManager(app)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
