from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisismysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rt_20@localhost/bookfinder"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from bookfinder import routes
