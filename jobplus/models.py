# -*- coding:utf8 -*-
# 存放数据模型相关代码

from flask import url_for
from flask_login import UserMixin
# 使用 flask_login 进行用户的登入登出管理，需要 User 类继承 flask_login 的 UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# flask 底层库提供了生成哈希密码的函数和检测密码哈希和密码是否相等的函数

db = SQLAlchemy()  # 此处不传入 app，因为 app 还没有进行定义


class Base(db.Model):
    """ 所有 model 的一个基类，默认添加了时间戳 """
    __abstract__ = True  # 表示不要将这个类作为 Model 类

    # 以下两个时间戳都不需要自己进行维护
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, 
                           default=datetime.utcnow, 
                           onupdate=datetime.utcnow)


class User(Base, UserMixin):
    __tablename__ = 'user'

    """ 用数值表示角色，方便判断是否有权限 """
    ROLE_COMPANY = 10
    ROLE_SEEKER = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    # unique:表示该值独一无二；index:添加之后便于提高运行速度；nullable:表示该值不为空
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    # 默认情况下，sqlalchemy 会以字段名来定义列名，但这里是 _password，为似有字段，故需明确的指定数据库名为 password
    role = db.Column(db.SmallInteger, default=ROLE_SEEKER)
    seeker_info = db.relationship('Seeker', uselist=False)
    company_info = db.relationship('Company', uselist=False)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):  # 该密码才是对外暴露的部分
        """ Python 风格的 getter """
        return self._password

    @password.setter
    def password(self, orig_password):
        """ Python 风格的 setter，这样设置 user.password 就会自动为 password 声称哈希值并存入 _password 字段 """
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        """ 判断用户输入的密码和存储的 hash 密码是否相等 """
        return check_password_hash(self._password, password)

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN


class Seeker(Base):
    __tablename__ = 'seeker'

    # 注册用户时性别， 教育多为选项，故先在前面进行设立
    G_MALE = 10
    G_FEMALE = 20

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    gender = db.Column(db.SmallInteger, default=G_MALE, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(256))  # 个人主页的图像
    education = db.Column(db.String(8), nullable=False)
    college = db.Column(db.String(128), nullable=False) 
    major = db.Column(db.String(128), nullable=False)
    working_years = db.Column(db.Integer)
    current_position = db.Column(db.String(128))
    except_position = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<Seeker:{}>'.format(self.name)


class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))
    logo = db.Column(db.String(256))  # url 地址
    company_name = db.Column(db.String(128), unique = True, index=True, nullable=False)
    offical_websit = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(256))
    industry = db.Column(db.String(16))
    stage = db.Column(db.String(16))
    city = db.Column(db.String(16))
    address = db.Column(db.String(128))
    # 在招职位
    position_num = db.Column(db.Integer)
    company_TEL = db.Column(db.String(16))
    job_list = db.relationship('Job', uselist=False)


    def __repr__(self):
        return '<Company:{}>'.format(self.name)

    @property
    def url(self):
        return url_for('company.detail', id=self.id)

class Job(Base):
    __tablename__ = 'job'

    EDU_COLLEGE = 10
    EDU_BACHELOR = 20
    EDU_MASTER = 30
    EDU_PHD = 40
    EDU_NOLIMIT = 60

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete="CASCADE"))
    job_name = db.Column(db.String(32), index=True, nullable=False)
    wage_area = db.Column(db.String(32), nullable=False)
    working_date_required = db.Column(db.String(16))
    experience_required = db.Column(db.String(256), nullable=False)
    edu_required = db.Column(db.SmallInteger, default=EDU_NOLIMIT)
    working_address = db.Column(db.String(16), nullable=False)
    company_info = db.relationship('Company')

    release_date = db.Column(db.String(32))

    job_description = db.Column(db.String(256))

    @property
    def url(self):
        return url_for('job.detail', id=self.id)

    def __repr__(self):
        return '<Job:{}>'.format(self.name)
