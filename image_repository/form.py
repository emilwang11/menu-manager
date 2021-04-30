from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class EditForm(FlaskForm):
    class Meta:
        csrf = False
    """Contact form."""
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


# @app.route("/edit/<product_id>")
# def edit(product_id):
#     return render_template("edit.html")
# class editproduct(FlaskForm):
#     edit_name = StringField('Product Name', validators=[DataRequired()])
#     edit_desc = StringField('Product Name', validators=[DataRequired()])

#     edit_qty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000),DataRequired()])
#     edit_submit = SubmitField('Save Changes')

