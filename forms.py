from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators


def mi_validacion(form, field):
    if (len(field.data) == 0):
        raise validators.ValidationError('El campo no tiene datos....')


class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 10, message = 'Long de campo 4 min y 5 max')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message = 'El campo es requerido')
    ])
    amaterno = StringField('Amaterno', [mi_validacion])
    apaterno = StringField('Apaterno')
    email = StringField('Correo')


class LoginForm(Form):
    username = StringField('Usuario', [
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 10, message = 'Long de campo 4 min and 10 max')
    ])

    password = StringField('Password', [
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 10, message = 'Long de campo 4 min and 10 max')
    ])


class FormIngresoPalabras(Form):
    palabraEspanol = StringField('Español:', [
        validators.DataRequired(message = 'El campo es requerido')
    ])

    palabraIngles = StringField('Inglés:', [
        validators.DataRequired(message = 'El campo es requerido')
    ])


class FormTraductor(Form):
    palabraTraducir = StringField('¿Cuál es la palabra qué deseas traducir?', [
        validators.DataRequired(message = 'El campo es requerido')
    ])