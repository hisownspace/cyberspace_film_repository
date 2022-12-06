from wtforms import StringField, IntegerField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange, Length, URL, ValidationError
from datetime import datetime
from urllib.request import urlopen

class FilmForm(FlaskForm):
  title = StringField(validators=[DataRequired()])
  year = IntegerField(validators=[NumberRange(1902, datetime.now().year)])
  plot = TextAreaField(validators=[Length(max=2000)])
  image_url = StringField(validators=[DataRequired(), Length(max=1000), URL(require_tld=True, message="Photo must ve a valid URL!")])
  genre_id = IntegerField()
  castIds = StringField()

def validate_image_url(form, field):
  try:
    content_type = urlopen(field.data).info()["content-type"]
  except:
    raise ValidationError("Must be a valid URL.")
  if "image" not in content_type:
    raise ValidationError("Photo must be a valid image URL!")
  return False