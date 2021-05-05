from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, FloatField, DecimalField, SubmitField
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
