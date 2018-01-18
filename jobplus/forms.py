from flask_wtf import FlaskForm  # FlaskForm 为每一个表单(html表单)输入声明一个字段
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required  # validators 添加了验证


class Company_RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3,24)])  # 验证长度，即限定长度
    email = StringField('邮箱', validators=[Required(), Email()])  # 必须符合 email 的格式
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')
    # Field一般提供两个参数，第一个是 html 中的标签，第二个是 validators, 表单提交的时候，会使用验证器进行验证，验证出现错误的将写入 Field 下的 Errors 列表


class Seeker_RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3,24)])  # 验证长度，即限定长度
    email = StringField('邮箱', validators=[Required(), Email()])  # 必须符合 email 的格式
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

