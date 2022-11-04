import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY='9892b398j38989bhi7b30gg332'
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'data.sqlite')