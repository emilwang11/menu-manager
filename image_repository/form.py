from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class EditForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField(
        'Name',
        [DataRequired()]
    )
    description = TextAreaField(
        'Description',
    )
    price = FloatField(
        'Price',
        [DataRequired()]
    )
    stock = IntegerField(
        'Stock',
        [DataRequired()]
    )
    submit = SubmitField('Submit')
