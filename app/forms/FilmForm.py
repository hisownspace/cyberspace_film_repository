from wtforms import StringField, IntegerField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange, Length
from datetime import datetime

class FilmForm(FlaskForm):
  title = StringField(validators=[DataRequired()])
  year = IntegerField(validators=[NumberRange(1902, datetime.now().year)])
  plot = TextAreaField(validators=[Length(max=2000)])
  photo_url = StringField(validators=[Length(max=1000)])
  genre_id = IntegerField()
  cast = StringField()