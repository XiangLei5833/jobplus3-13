# /usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import time
import csv
import random
import json
from lxml import etree

proxies = {
        'https':'https://115.226.11.248:808',
        'https':'https://200.159.136.16:53286',
        'https':'https://122.53.183.83:8080',
        'https':'https://124.81.121.62.8080'
        }


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    }

cookies = {
    'Cookie': 'user_trace_token=20180125175402-9ea64eb2-4573-4535-b377-f3d84c1877e0;'
    ' _ga=GA1.2.1136621226.1516874047;'
    ' LGUID=20180125175407-af00f512-01b5-11e8-ab94-5254005c3644;' 
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516937239,1517212801,1517213234,1517213303; _gid=GA1.2.887105809.1517212803; '
    'ab_test_random_num=0; showExpriedIndex=1; '
    'showExpriedCompanyHome=1; showExpriedMyPublish=1; '
    'hasDeliver=0; gate_login_token=ce202aed5d506a0b9599677b6b0dd99d1af1020ce48aeaaa; '
    'index_location_city=%E5%85%A8%E5%9B%BD; '
    'JSESSIONID=ABAAABAACDBABJBDB6BA31AEA9EB69EDBF080637CE2B0ED; '
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517217240; '
    'LGRID=20180129171357-bc61a837-04d4-11e8-a04b-525400f775ce; '
    '_putrc=452664D9C667AAD1; '
    'login=true; '
    'unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B75833; '
    'TG-TRACK-CODE=index_search; gate_login_token=""; '
    'X_HTTP_TOKEN=5aff0cdc856cc5faa670acc39f9347ac; '
    '_gat=1; LGSID=20180129171255-97734b29-04d4-11e8-abd1-5254005c3644; '
    'PRE_UTM=; '
    'PRE_HOST=; '
    'PRE_SITE=; '
    'PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; '
    'SEARCH_ID=7f11ff6c7e5648f6b79f24ff4709d96c' 
}
    
data = {
    'first': True,
    'pn':1,
}


def get_job(data):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false&isSchoolJob=0'
    page = requests.post(url=url, cookies=cookies, headers=headers, data=data)
    page.encoding = 'utf-8'
    result = page.json()
    jobs = result['content']['positionResult']['result']
    f = open('../jobplus3-13/datas/jobs.txt', 'a+')    
    for job in jobs:
        positionId = job['positionId']  # 主页ID
        companyId = job['companyId']  # 公司ID
        print(job, file=f)

#        job_detail_url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
#        job_response = requests.get(url=job_detail_url, headers=headers, cookies=cookies)
#        job_response.encoding = 'utf-8'
#        job_tree = etree.HTML(job_response.text)
#        job_desc = job_tree.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
#      # addr = (tree.xpath('//*[@id="job_detail"]//dd[3]/div[1]/a[1]/text()'))[0].replace('\'','')+(tree.xpath('//*[@id="job_detail"]//dd[3]/div[1]/a[2]/text()'))[0].replace('\'','')+((tree.xpath('//*[@id="job_detail"]//dd[3]/div[1]/text()'))[3].replace('\n','')).strip()
#        for job_des in job_desc:
#            print(job_des, file=f)
#
#        company_detail_url = 'https://www.lagou.com/gongsi/{}.html'.format(companyId)
#        company_response = requests.get(url=job_detail_url, headers=headers, cookies=cookies)
#        company_response.encoding = 'utf-8'
#        company_tree = etree.HTML(company_response.text)
#        company_desc = company_tree.xpath('//*[@id="company_intro"]/div[2]/div/span[1]/p/text()')
#        for company_des in company_desc:
#            print(company_des, file=f)
    f.close()

def url(data):
    for x in range(1,50):
        data['pn'] = x
        get_job(data)

if __name__ == '__main__':
    url(data)
