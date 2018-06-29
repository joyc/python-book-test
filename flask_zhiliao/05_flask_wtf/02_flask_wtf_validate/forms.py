from wtforms import Form, StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import Length, EqualTo, Email, InputRequired, \
    NumberRange, Regexp, URL, UUID, ValidationError


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10,
        message="用户名长度必须在3到10位之间")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=6, max=10),
        EqualTo("password")])


class LoginForm(Form):
    # email = StringField(validators=[Email()])
    # username = StringField(validators=[InputRequired()])
    # age = IntegerField(validators=[NumberRange(18, 100)])
    # phone = StringField(validators=[Regexp(r'1[38745]\d{9}')])
    # homepage = StringField(validators=[URL()])
    # uuid = StringField(validators=[UUID()])
    
    # 自定义验证
    captcha = StringField(validators=[Length(4, 4)])
    def validate_captcha(self, field):
        # print(field.data)
        if field.data != '1234':
            raise ValidationError('验证码错误')


class SettingsForm(Form):
    username = StringField("用户名: ", validators=[InputRequired()])
    age = IntegerField("年龄: ", validators=[NumberRange(10, 100)])
    remember = BooleanField("记住我: ")
    tags = SelectField("选项: ", choices=[('1',"python"), ('2',"ios")])


