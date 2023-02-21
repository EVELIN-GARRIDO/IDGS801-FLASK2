from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 10, message = 'Long de campo 4 min y 5 max')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message = 'El campo es requerido')
    ])
    amaterno = StringField('Amaterno')
    apaterno = StringField('Apaterno')
    email = StringField('Correo')
