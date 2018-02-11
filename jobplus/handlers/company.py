from flask import Blueprint, render_template, flash, request, current_app, redirect, url_for
from flask_login import current_user
from jobplus.forms import CompanyForm, JobForm
from jobplus.models import db, Company, Job, User
from jobplus.decorators import admin_required

company = Blueprint('company', __name__, url_prefix='/companys')

@company.route('/profile', methods=['GET', 'POST'])
def profile():
    form = CompanyForm()
    if form.validate_on_submit():
        form.create_company()
        flash('已保存', 'success')
    return render_template('company_main.html', form=form)

@company.route('/create', methods=['GET', 'POST'])
def create_job():
    form = JobForm()
    if form.validate_on_submit():
        form.create_job()
        flash('职位创建成功', 'success')
        return redirect(url_for('company.manage'))
    return render_template('company/create_job.html', form=form)
    
@company.route('/manage')
def manage():
    if Company.query.filter_by(user_id=current_user.id).first():
        company = Company.query.filter_by(user_id=current_user.id).first()
        jobs = Job.query.filter_by(company_id=company.id)
    return render_template('company/manage.html', jobs=jobs)

@company.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_job(id):
    job = Job.query.get_or_404(id)
    form = JobForm(obj=job)
    if form.validate_on_submit():
        form.update_company(job)
        flash('课程更新成功', 'success')
        return redirect(url_for('company.manage'))
    return render_template('company/edit_job.html', form=form, job=job)

@company.route('/<int:id>/delete')
def delete_job(id):
    job = Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    flash('职位删除成功', 'success')
    return redirect(url_for('company.manage'))

@company.route('/')
def company_list():
    # 获取参数中传过来的页数
    page = request.args.get('page', default=1, type=int)
    # 生成分页对象
    pagination = Company.query.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False
            )
    return render_template('company_list.html', pagination=pagination)

@company.route('/<int:id>')
def detail(id):
    company = Company.query.get_or_404(id)
    return render_template('company/detail.html', company=company)
