import os
from random import randint
from faker import Faker
from jobplus.models import db, Company, User

faker = Faker()  # 创建 faker 工厂对象，生成一个用于测试数据的库

jobs = open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'jobs.txt'))

def iter_companys():
    for user in User.query:
        for company in jobs:
            company = eval(company)
            yield Company(
                logo = '//www.lgstatic.com/thumbnail_160x160/'+company['companyLogo'],
                company_name = company['companyShortName'],
                industry = company['industryField'],
                stage = company['financeStage'],
                city = company['city'],
                welfare = str(company['companyLabelList']),
                company_size = company['companySize'],
                company_attr = company['secondType'],
                user=user
                )
            break

def run():    
    for company in iter_companys():
        db.session.add(company)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
#jobs.close()
