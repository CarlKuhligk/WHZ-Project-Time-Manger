from flask import Flask
from .models._base import Base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(model_class=Base)