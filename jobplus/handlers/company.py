
from flask import Blueprint, render_template, flash, request, current_app
from jobplus.forms import CompanyForm
from jobplus.models import Company

company = Blueprint('company', __name__, url_prefix='/companys')

@company.route('/profile', methods=['GET', 'POST'])
def profile():
    form = CompanyForm()
    if form.validate_on_submit():
        form.create_company()
        flash('已保存', 'success')
    return render_template('company_main.html', form=form)

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
