from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('username', validators = [DataRequired()])
  password = PasswordField('Password', validators =[DataRequired()])
  remember_me = BooleanField('Remember me')
  submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
  username = StringField('username', validators = [DataRequired()])
  email = StringField('email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validator=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data)