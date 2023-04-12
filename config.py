import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
    Flask_APP = os.environ.get('FLASK_APP')
    Flask_ENV = os.environ.get('FLASK_ENV')