from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class CupcakeForm(FlaskForm):
    flavor = StringField('Flavor', validators=[InputRequired()])
    size = StringField('Size', validators=[InputRequired()])
    rating = FloatField('Rating', validators=[InputRequired()])
    image = StringField('Image URL', validators=[URL()])