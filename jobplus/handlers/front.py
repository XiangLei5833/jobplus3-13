# 注册蓝图，将主页路由移入其中

from flask import Blueprint, render_template

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')
