from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = IntegerField("ID руководителя", validators=[DataRequired()])
    job = StringField("Описание работы", validators=[DataRequired()])
    work_size = IntegerField("Часы", validators=[DataRequired()])
    collaborators = StringField("Участники (id через запятую)")
    is_finished = BooleanField("Завершена")
    submit = SubmitField("Добавить работу")
