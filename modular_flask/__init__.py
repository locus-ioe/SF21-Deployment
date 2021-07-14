from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

from . import routes  # noqa

if __name__ == "__main__":
  print("Creating Database...")
  db.create_all()
  print("Database Created!")