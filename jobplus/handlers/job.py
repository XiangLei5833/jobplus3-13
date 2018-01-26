from flask import Blueprint, render_template
from jobplus.models import Job, Company

job = Blueprint('job', __name__, url_prefix='/jobs')

@job.route('/<int:id>')
def detail(id):
    company = Company.query.get_or_404(id)
    return render_template('job/detail.html', job=job)

@job.route('/')
def job_list():
    # 获取参数中传过来的页数
    page = request.args.get('page', default=1, type=int)
    # 生成分页对象
    pagination = Job.query.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False
            )
    return render_template('job_list.html', pagination=pagination)
