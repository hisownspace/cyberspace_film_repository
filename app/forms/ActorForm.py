from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError, Optional
from urllib.request import urlopen

class ActorForm(FlaskForm):
  class Meta:
    csrf = False


  name = StringField("Name", [DataRequired(), Length(min=3, max=255)])
  date_of_birth = DateField("Date of Birth", [DataRequired()])
  place_of_birth = StringField("Place of Birth", [Optional(), Length(min=2, max=255)])
  photo = StringField("Photo", [DataRequired(), URL(require_tld=True, message="Photo must be a valid URL!")])
  
  def validate_photo(form, field):
    try:
      content_type = urlopen(field.data).info()["content-type"]
    except:
      return      
    if "image" not in content_type:
      raise ValidationError("Photo must be a valid image URL!")
    return False