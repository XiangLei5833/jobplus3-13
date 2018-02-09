from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from jobplus.models import Company, Job
from jobplus.decorators import admin_required
from jobplus.forms import CompanyForm, JobForm, db

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

@admin.route('/company')
@admin_required
def companys():
    page = request.args.get('page', default=1, type=int)
    pagination = Company.query.paginate(
            page=page,
            per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out=False
            )
    return render_template('admin/companys.html', pagination=pagination)

@admin.route('/job')
@admin_required
def jobs():
    page = request.args.get('page', default=1, type=int)
    pagination = Job.query.paginate(
            page=page,
            per_page=current_app.config['ADMIN_PER_PAGE'],
            error_out=False
            )
    return render_template('admin/jobs.html', pagination=pagination, Company=Company)

@admin.route('/company/<int:id>/edit', methods=['GET','POST'])
@admin_required
def edit_company(id):
    company = Company.query.get_or_404(id)
    form = CompanyForm(obj=company)
    if form.validate_on_submit():
        form.update_company(company)
        flash('公司更新成功', 'success')
        return redirect(url_for('admin.companys'))
    return render_template('admin/edit_company.html', form=form, company=company)

@admin.route('/company/<int:id>/delete')
@admin_required
def delete_company(id):
    company = Company.query.get_or_404(id)
    db.session.delete(company)
    db.session.commit()
    flash('公司删除成功', 'success')
    return redirect(url_for('admin.companys'))

@admin.route('/job/<int:company_id>/edit', methods=['GET','POST'])
@admin_required
def edit_job(company_id):
    job = Job.query.get_or_404(company_id)
    form = JobForm(obj=job)
    if form.validate_on_submit():
        form.update_job(job)
        flash('职位更新成功', 'success')
        return redirect(url_for('admin.jobs'))
    return render_template('admin/edit_job.html', form=form, job=job)

@admin.route('/job/<int:company_id>/delete')
@admin_required
def delete_job(company_id):
    job = Job.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    flash('职位删除成功', 'success')
    return redirect(url_for('admin.jobs'))
