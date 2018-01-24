from flask import Blueprint, render_template, flash
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

@company.route('/<int:company_id>')
def detail(company_id):
    company = Company.query.get_or_404(company_id)
    return render_template('company/detail.html', company=company)
