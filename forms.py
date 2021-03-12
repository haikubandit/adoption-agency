from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length



# FORMS GO BELOW!

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet name cannot be blank")])
    species = SelectField(
        "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[URL(message="Not a valid URL"),
         Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Age must be between 0 and 30"), Optional()])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")