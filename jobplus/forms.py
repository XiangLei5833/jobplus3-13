from flask_wtf import FlaskForm  # FlaskForm 为每一个表单(html表单)输入声明一个字段
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required  # validators 添加了验证
from jobplus.models import db, User



class Company_RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3,24)])  # 验证长度，即限定长度
    email = StringField('邮箱', validators=[Required(), Email()])  # 必须符合 email 的格式
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')
    # Field一般提供两个参数，第一个是 html 中的标签，第二个是 validators, 表单提交的时候，会使用验证器进行验证，验证出现错误的将写入 Field 下的 Errors 列表

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class Seeker_RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3,24)])  # 验证长度，即限定长度
    email = StringField('邮箱', validators=[Required(), Email()])  # 必须符合 email 的格式
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
    
    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')
