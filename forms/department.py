from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    chief = IntegerField("ID начальника", validators=[DataRequired()])
    members = StringField("Участники (id через запятую)")
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Добавить департамент")
