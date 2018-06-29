from wtforms import Form, FileField, StringField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import InputRequired


class UploadForm(Form):
    avatar = FileField(validators=[FileRequired(), FileAllowed(['jpg', \
        'png', 'gif'])])
    desc = StringField(validators=[InputRequired()])
