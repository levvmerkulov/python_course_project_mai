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
    POSTS_PER_PAGE = 5
    POSTS_PER_PAGE_USER = 3

    #Enable email notifications
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['warfishe@yandex.ru']   