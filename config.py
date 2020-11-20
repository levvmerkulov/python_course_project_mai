import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    #Enabling MYSQL
    
    MYSQL_HOST = 'localhost'
    
    MYSQL_USER = 'root'
    
    MYSQL_PASSWORD = 'password'
    
    #database to use
    MYSQL_DB = 'flask_mai'

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #'sqlite:///' + os.path.join(basedir, 'app.db')

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #   'mysql://root:password' os.path.join(basedir, 'app.db') 

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/flask_mai'
    SQLALCHEMY_TRACK_MODIFICATIONS = False