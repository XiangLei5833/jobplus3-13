# 存放数据模型相关代码

from flask_login import UserMixin
# 使用 flask_login 进行用户的登入登出管理，需要 User 类继承 flask_login 的 UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.seurity import generate_password_hash, check_password_hash
# flask 底层库提供了生成哈希密码的函数和检测密码哈希和密码是否相等的函数

db = SQLAlchemy()  # 此处不传入 app，因为 app 还没有进行定义


class Base(db.Model):
    """ 所有 model 的一个基类，默认添加了时间戳 """
    __abstract__ = True  # 表示不要将这个类作为 Model 类

    # 以下两个时间戳都不需要自己进行维护
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base, UserMixin):
    __tablename__ = 'user'


