from wtforms import StringField, IntegerField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from datetime import datetime
# from urllib.request import urlopen

from app.api.aws_helper import ALLOWED_EXTENSIONS

class FilmForm(FlaskForm):
  title = StringField(validators=[DataRequired()])
  year = IntegerField(validators=[NumberRange(1902, datetime.now().year)])
  plot = TextAreaField(validators=[Length(max=2000)])
  image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
  genre_id = IntegerField()
  castIds = StringField()

# def validate_photo_url(form, field):
#   try:
#     content_type = urlopen(field.data).info()["content-type"]
#   except:
#     raise ValidationError("Must be a valid URL.")
#   if "image" not in content_type:
#     raise ValidationError("Photo must be a valid image URL!")
#   return False
