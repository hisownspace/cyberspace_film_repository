from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class ActorForm(FlaskForm):
  name = StringField("Name", [DataRequired(), Length(min=3, max=255)])
  date_of_birth = DateField("Date of Birth", [DataRequired()])
  place_of_birth = StringField, [Length(min=2, max=255)]
  photo = StringField("Photo", [DataRequired()])
  
  def photo_validator(form, field):
    pass