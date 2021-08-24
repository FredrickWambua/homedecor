from flask_wtf import FlaskForm
from wtfforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User