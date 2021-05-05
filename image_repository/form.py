from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class EditForm(FlaskForm):
    class Meta:
        csrf = False
    name = StringField(
        'Name',
        [DataRequired()]
    )
    description = TextField(
        'Description',
        [
            DataRequired(),
            Length(min=4,
            message=('Your description is too short.'))
        ]
    )
    submit = SubmitField('Submit')

