from flask_wtf import FlaskForm  # FlaskForm 为每一个表单(html表单)输入声明一个字段
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required  # validators 添加了验证
from jobplus.models import db, User, Seeker, Company, Job



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


class SeekerForm(FlaskForm):
    SEX_TYPE = [
            ('male', '男'),
            ('female', '女')
            ]
    EDU = [
            ('college', '大专'),
            ('bachelor', '本科'),
            ('master', '硕士'),
            ('phd', '博士'),
            ('other', '其他')
            ]
    name = StringField('姓名', validators=[Required(), Length(2,24)])
    gender = SelectField('性别', choices=SEX_TYPE)
    age = StringField('年龄', validators=[Required(), Length(1,2)])
    education = SelectField('学历', choices=EDU)
    college = StringField('毕业院校', validators=[Required(), Length(4,30)])
    major = StringField('专业', validators=[Required(), Length(4,30)])
    working_years = StringField('工作年限', validators=[Required(), Length(1,2)])
    current_position = StringField('当前岗位', validators=[Required(), Length(3,24)])
    except_position = StringField('期待岗位', validators=[Required(), Length(3,24)])
    submit = SubmitField('保存')

    def create_seeker(self):
        seeker = Seeker()
        seeker.name = self.name.data
        seeker.gender = self.gender.data
        seeker.age = self.age.data
        seeker.education = self.education.data
        seeker.college = self.college.data
        seeker.major = self.major.data
        seeker.working_years = self.working_years.data
        seeker.current_position = self.current_position.data
        seeker.except_position = self.except_position.data
        db.session.add(seeker)
        db.session.commit()
        return seeker


class CompanyForm(FlaskForm):
    name = StringField('公司名称', validators=[Required(), Length(3,24)])
    offical_websit = StringField('官网', validators=[Required(), Length(3,50)])
    address = StringField('公司地址', validators=[Required(), Length(3,50)])
    company_TEL = StringField('公司电话', validators=[Required(), Length(11, 13)])
    description = StringField('公司描述', validators=[Required(), Length(10, 100)])
    submit = SubmitField('保存')

    def create_company(self):
        company = Company()
        company.name = self.name.data
        company.offical_websit = self.offical_websit.data
        company.address = self.offical_websit.data
        company.company_TEL = self.company_TEL.data
        company.description = self.dexcription.data
        db.session.add(company)
        db.session.commit()
        return company

    def validate_name(self, field):
        if Company.query.filter_by(name=field.data).first():
            raise ValidationError('公司已经存在')
