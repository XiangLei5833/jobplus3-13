# 注册蓝图，将主页路由移入其中

from flask import Blueprint, render_template
from jobplus.forms import LoginForm, Seeker_RegisterForm, Company_RegisterForm

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)  # form由此传递入 login.html

@front.route('/C-register')
def company_register():
    form = Company_RegisterForm()
    return render_template('company_register.html', form=form)

@front.route('/S-register')
def seeker_register():
    form = Seeker_RegisterForm()
    return render_template('seeker_register.html', form=form)
