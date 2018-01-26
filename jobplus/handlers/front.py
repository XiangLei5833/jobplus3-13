# 注册蓝图，将主页路由移入其中

from flask_login import login_user, logout_user, login_required
from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from jobplus.forms import LoginForm, Seeker_RegisterForm, Company_RegisterForm
from jobplus.models import User, Company, Job

front = Blueprint('front', __name__)

@front.route('/')
def index():
    companys = Company.query.filter().limit(9)
    jobs = Job.query.filter().limit(9)
    return render_template('index.html', companys=companys, jobs=jobs)

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)  # 第一个参数 User 对象，跌入个参数布尔值，告诉 flask_login 是否要记住该用户
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)  # form由此传递入 login.html

@front.route('/logout')
@login_required  # login_required 装饰器保护了这个路由处理函数，未登录状态下访问这个页面会被重定向到登录页面
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('.index'))

@front.route('/C-register', methods=['GET', 'POST'])
def company_register():
    form = Company_RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功， 请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('company_register.html', form=form)

@front.route('/S-register', methods=['GET', 'POST'])
def seeker_register():
    form = Seeker_RegisterForm()
    if form.validate_on_submit():  # from.validate.submit是 flask_wtf 提供的封装方法，返回布尔值
        form.create_user()
        flash('注册成功， 请登录！', 'success')  # flash() 向模板页面发送一个消息，两个参数，消息内容和分类
        return redirect(url_for('.login'))
    return render_template('seeker_register.html', form=form)

