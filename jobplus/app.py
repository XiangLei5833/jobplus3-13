# -*- coding:utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from jobplus.config import configs
from jobplus.models import db, User
from flask_migrate import Migrate

def register_blueprints(app):
    from .handlers import front, seeker, company, job, admin, tests
    app.register_blueprint(front)
    app.register_blueprint(seeker)
    app.register_blueprint(company)
    app.register_blueprint(job)
    app.register_blueprint(admin)
    app.register_blueprint(tests)

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader  # 使用 user_login 装饰器注册一个函数，用来告诉 flask-login 如何加载用户对象
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'  # login_view设置的为登录页面的路由，有它，当用 flask-login 提供的 login_required 装饰器保护一个路由时候，用户未登录，就会被重定向到指定页面

def create_app(config):
    """ App 工厂 """
    """ 可以根据传入的 config 名称，加载不同的配置 """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)
    register_extensions(app)

    return app
