from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField

class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    amaterno = StringField('Amaterno')
    apaterno = StringField('Apaterno')
    email = StringField('Correo')
