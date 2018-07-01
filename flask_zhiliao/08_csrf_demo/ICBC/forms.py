from wtforms import Form, StringField, FloatField
from wtforms.validators import Email, EqualTo, Length, InputRequired, \
    NumberRange
from models import User


class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3, 20)])
    password = StringField(validators=[Length(6, 20)])
    password_repeat = StringField(validators=[EqualTo("password")])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    password = StringField(validators=[Length(6, 20)])

    # 检验邮箱密码是否正确即用户存在于数据库
    # def validate(self):
    #     # 先看父类的格式验证是否正确
    #     result = super(LoginForm, self).validate()
    #     if not result:
    #         return False
    #
    #     email = self.email.data
    #     password = self.password.data
    #     user = User.query.filter(User.email == email,
    #                              User.password == password).first()
    #     if not user:
    #         # 没有的话往errors列表中添加错误信息
    #         self.email.errors.append('邮箱或者密码错误！')
    #         return False
    #     return True


class TransferForm(Form):
    email = StringField(validators=[Email()])
    money = FloatField(validators=[NumberRange(1, 1000000)])
