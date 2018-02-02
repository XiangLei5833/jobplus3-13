import os
from random import randint
from faker import Faker
from jobplus.models import db, User, Company, Seeker, Job

faker = Faker()  # 创建 faker 工厂对象，生成一个用于测试数据的库

jobs = open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'jobs.txt'))

def iter_jobs():
    for company in Company.query:
        for job in jobs:
            job = eval(job)
            if job['companyShortName'] == company.company_name:
                yield Job(
                    job_name = job['positionName'],
                    wage_area = job['salary'],
                    working_address = job['city'],
                    experience_required = job['workYear'],
                    edu_required = job['education'],
                    release_date = job['formatCreateTime'],
                    job_tempt = job['positionAdvantage'],
                    job_attr = job['firstType'],
                    job_nature = job['jobNature'],
                    company = company
                    )
                break


def run():

    for job in iter_jobs():
        db.session.add(job)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
#jobs.close()
