from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# generate an instance of Class Flask
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from decrypt import views, models
