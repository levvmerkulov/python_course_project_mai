from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,\
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, \
    Length, EqualTo
from app.models import User, Post

class LoginForm(FlaskForm):
    '''sign-in form on web page'''
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember me!')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    """sign-up form on web page"""
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField(
        'Repeat Password', 
        validators = [DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Please use another username')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Please use another email')

class EditProfileForm(FlaskForm):
    '''edit user profile'''
    username = StringField('Username', validators = [DataRequired()])
    about_me = StringField('About me', validators = [Length(min = 0,
        max = 140)])
    submit = SubmitField('Submit changes')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username = self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username')

class PostForm(FlaskForm):
    '''post messages about Brown/Green-field approach at profile page'''
    post = TextAreaField('Добавьте факт о подходах!', validators = [DataRequired(),
        Length(min = 1, max = 280)])
    submit = SubmitField('Submit')

    """def validate_content(self, post):
        word = 'подход'
        if not word in post.data:
            raise ValidationError('Please correct your information!')"""

class ShowPostForm(FlaskForm):
    '''show one random post at once'''
    submit = SubmitField('Get random fact!')
    """    cnt = len(Post.query.all())
    rand_num = random.randint(1, cnt)
    post = Post.query.get(rand_num)"""