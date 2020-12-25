from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import jwt
from time import time 
from hashlib import md5
from app import db, login, app_name

class User(UserMixin, db.Model):
    '''users table. UserMixin imports Flask-Login requirements'''
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default = datetime.utcnow)
    #one-to-many relationship
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        '''this method tells how to print users'''
        return '<User {} -- {}>'.format(self.username, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
    
    def get_reset_password_token(self, expires_in = 600):
        '''get jwt token to reset pass'''
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in}, 
            app_name.config['SECRET_KEY'],
            algorithm = 'HS256'
        ).decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(
                token, 
                app_name.config['SECRET_KEY'], 
                algorithms = ['HS256']
            )['reset_password']
        except:
            return
        return User.query.get(id)

class Post(db.Model):
    """posts table"""
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, index = True, \
        default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '< Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    '''reloads a user from the session'''
    return User.query.get(int(id))