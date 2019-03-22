from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField

from wtforms.validators import DataRequired,Email


class ContactForm(FlaskForm):
    name = StringField("Enter Fullname", validators=[DataRequired()])
    email = StringField("Enter your Email", validators=[DataRequired()])
    message =TextAreaField("Type Message Here", validators=[DataRequired()])
    submit = SubmitField("Submit")

