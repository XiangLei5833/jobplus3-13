import os
import json
from random import randint
from faker import Faker
from jobplus.models import db, User, Company, Seeker, Job

faker = Faker()  # 创建 faker 工厂对象，生成一个用于测试数据的库

with open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'jobs.json')) as f:
    jobs = json.load(f)

def iter_companys():
    for company in jobs:
        yield Company(
                logo = company['logo'],
                company_name = company['company_name'],
                offical_websit = company['offical_websit'],
                industry = company['industry'],
                stage = company['stage'],
                city = company['city']
                )

def iter_jobs():
    for job in jobs:
        yield Job(
            job_name = job['jobname'],
            wage_area = job['wage_area'],
            working_address = job['working_address'],
            experience_required = job['experience'],
            edu_required = job['education'],
            release_date = job['release_date']
            )

def run():
    for company in iter_companys():
        db.session.add(company)

    for job in iter_jobs():
        db.session.add(job)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
                

