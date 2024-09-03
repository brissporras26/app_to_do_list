#formularios de entrada usando Flask-WTF

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Lenght(min=4, max=25)])
    password = PasswordField('Contraseña', validators = [DataRequired()])
    bmitField('Inciar Sesion')


class TaskForm(FlaskForm):
    task =  StringField('Tarea', validators=[DataRequired()])
    priority =  SelectField('Prioridad', choices = [('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')])
    image = FileField('Subir Imagen')
    submit = SubmitField('Añadir Tarea')
