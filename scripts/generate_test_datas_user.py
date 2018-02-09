import os
from random import randint
from faker import Faker
from jobplus.models import db, User

faker = Faker()  # 创建 faker 工厂对象，生成一个用于测试数据的库

jobs = open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'jobs.txt'))

def iter_users():
    for user in jobs:
        user = eval(user)
        yield User(
                username = user['companyShortName'],
                email = str(user['lastLogin'])+'@example.com',
                password = 'frefvr',
                role = 10,
                )   

def run():
    for user in iter_users():
        db.session.add(user)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

