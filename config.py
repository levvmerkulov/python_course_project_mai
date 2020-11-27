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

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/flask_mai'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Pagination options
    POSTS_PER_PAGE = 3