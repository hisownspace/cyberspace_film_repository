from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField, FieldList, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Length, URL, ValidationError, Optional
from urllib.request import urlopen

class ActorForm(FlaskForm):
  # class Meta:
  #   csrf = False

  name = StringField("Name", [DataRequired(), Length(min=3, max=255)])
  date_of_birth = DateField("Date of Birth", [DataRequired()])
  place_of_birth = StringField("Place of Birth", [Optional(), Length(min=2, max=255)])
  photo_url = StringField("Photo", [DataRequired(), URL(require_tld=True, message="Photo must be a valid URL!")])
  bio = StringField("String", [Length(max=5000)])
  filmography = SelectMultipleField("Films", choices=[], validate_choice=False, coerce=int)
  
  def validate_photo_url(form, field):
    try:
      content_type = urlopen(field.data).info()["content-type"]
    except:
      raise ValidationError("Must be a valid URL.")
    if "image" not in content_type:
      raise ValidationError("Photo must be a valid image URL!")
    return False