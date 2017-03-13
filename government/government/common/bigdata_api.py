# coding=utf-8
__author__ = 'YANGJINHUA963'
import requests
import json


# get 请求
def get_data(url, request):
    r = requests.get(url, params=request)
    return r.text


# post 请求
def post_data():
    request = {'userCode': '800953490', 'productNo': 13, 'commissionBh': 60, 'accountType': '00', 'source': 5}
    r = requests.post('http://10.25.166.29:8080/ocrm-svc/private/v1/commission/sub', data=json.dumps(request))
    return r.text


# url = 'http://10.25.163.48/vast/vast_action_category/get'
# request_data = {'id': '10'}
# print get_data(url, request_data)
print post_data()
