from flask import Blueprint, render_template
from jobplus.forms import CompanyForm

company = Blueprint('company', __name__, url_prefix='/companys')

@company.route('/profile')
def profile():
    form = CompanyForm()
    if form.validate_on_submit():
        form.create_company()
        flash('已保存', 'success')
    return render_template('company_main.html', form=form)
