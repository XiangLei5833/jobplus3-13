from flask import Blueprint, render_template, flash, request, current_app
from jobplus.forms import CompanyForm, JobForm
from jobplus.models import Company, Job, User
from jobplus.decorators import admin_required

company = Blueprint('company', __name__, url_prefix='/companys')

@company.route('/profile', methods=['GET', 'POST'])
def profile():
    form = CompanyForm()
    if form.validate_on_submit():
        form.create_company()
        flash('已保存', 'success')
    return render_template('company_main.html', form=form)

@company.route('/createbefore')
def create_before():
    return render_template('company/create_job_before.html')

@company.route('/create', methods=['GET', 'POST'])
def create_job():
    form = JobForm()
    if form.validate_on_submit():
        form.create_job()
        flash('职位创建成功', 'success')
        return redirect(url_for('company.profile'))
    return render_template('company/create_job.html', form=form)
    
@company.route('/manage')
def manage():
    #job = Job.query.get_or_404(company_id)
    return render_template('company/manage.html')

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
