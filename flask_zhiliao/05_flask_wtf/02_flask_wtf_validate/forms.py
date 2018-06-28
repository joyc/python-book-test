from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, \
    Regexp, URL, UUID


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10,
                                              message="用户名长度必须在3到10位之间")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=6, max=10), EqualTo("password")])


class LoginForm(Form):
    # email = StringField(validators=[Email()])
    # username = StringField(validators=[InputRequired()])
    # age = IntegerField(validators=[NumberRange(18, 100)])
    # phone = StringField(validators=[Regexp(r'1[38745]\d{9}')])
    # homepage = StringField(validators=[URL()])
    uuid = StringField(validators=[UUID()])

