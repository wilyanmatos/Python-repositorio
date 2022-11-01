from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# As outras funções precisam dessa variável, por isso ela vem antes da importação
app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storage.db"

from app.controllers import default


