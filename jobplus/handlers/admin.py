from flask import Blueprint, render_template, request, current_app
from jobplus.models import Company, Job
from jobplus.decorators import admin_required

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

