from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField

class Cajas(Form):
    cantidadCajas = IntegerField('Cantidad cajas:')