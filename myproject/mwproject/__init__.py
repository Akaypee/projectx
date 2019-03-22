from flask import Flask

from .config import TestEnviroment 
from flask_wtf import CSRFProtect

app = Flask(__name__,instance_relative_config=True)

app.config.from_object(TestEnviroment)
app.config.from_pyfile('config.py', silent=True)

csrf = CSRFProtect()

csrf.init_app(app)

from mwproject import view