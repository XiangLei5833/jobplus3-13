# -*- coding:utf-8 -*-

from flask import Flask
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

def create_app(config):
    """ App 工厂 """
    """ 可以根据传入的 config 名称，加载不同的配置 """
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app, db)
    register_blueprints(app)

    return app
