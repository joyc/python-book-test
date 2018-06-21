<<<<<<< HEAD
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField('Submit')
=======
pass
>>>>>>> ef430b6090c81ca76a224436ec7407d340e1538d
