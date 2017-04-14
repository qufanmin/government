#coding:utf-8
# Create your tests here.
import json
import urllib2,urllib
import datetime
import httplib
import requests

class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

#"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
#"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
print hasattr(emp1, 'age')

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__


class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "销毁"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3) # 打印对象的id
del pt1
del pt2
del pt3

class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "调用父类构造函数"

   def parentMethod(self):
      print '调用父类方法'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "父类属性 :", Parent.parentAttr

class Child(Parent): # 定义子类
   def __init__(self):
      print "调用子类构造方法"

   def childMethod(self):
      print '调用子类方法 child method'

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法
print issubclass(Child,Parent)
print isinstance(c,Child)
print isinstance(c,Parent)


class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2


class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount

counter = JustCounter()
#counter.count()
#counter.count()
#print counter.publicCount
print counter._JustCounter__secretCount
print counter.__secretCount  # 报错，实例不能访问私有变量
'''
data={"mobileNos":"[\"\",\"13860770913\",\"13902938010\"]","source":"YDKH"}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
response=requests.post('http://10.25.163.13:30074/userservice/queryUserIdsByMobileNos',headers=headers,data=data)
print response.text
'''
'''
data={
                "mobileList": [
                                {
                                    "mobile": "13601692567",
                                    "context": {
                                                    "1": "刘华强",
                                                    "2": "2014年11月28日14：00",
                                                    "3": "金田路",
                                                    "4": "马云",
                                                    "5": "123456789012345E31",
                                                    "6": "上海陆家嘴环形路3322号海洋水族馆对面",
                                                    "7": "上海陆家嘴环形路3322号海洋水族馆对面"
                                                },
                                     "reqUuid": datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"huiaiw5"
                                }
                                ],
                "templateId": "ZQ_JJ160630001",
                "arrangeDate": "20160421031623",
                "operator": "屈凡民"
                }
'''
'''
data={
    "ad_name":"qufanmin",
    "adpos_id":54078,
    "adpos_name":"用户中心点击业务办理，点击转签创业板，再点击【同意协议并申请】按钮",
    "create_time":1479102663000,
    "create_um":"梨花",
    "delivery_flag":"2",
    "delivery_item":"[{\"key\":\"pama_open_date\",\"value\":\"unnull\",\"oper\":\"and\",\"$$hashKey\":\"object:5870\"}]",
    "delivery_sql":"select * from a",
    "delivery_ui":"{\"search\":{\"wheres\":[{\"key\":\"pama_open_date\",\"value\":\"unnull\"}],\"fields\":[\"cust_code\"],\"start\":1,\"end\":50,\"addition\":\"cust_type between 0 and 4 and priv_plac is null and non_trade is null\"},\"pro\":[{\"key\":\"cust_code\",\"name\":\"cust_code\",\"title\":\"客户代码\",\"type\":\"string\",\"value\":\"\",\"_private\":true},{\"title\":\"理财开户日期\",\"type\":\"date\",\"value\":\"unnull\",\"name\":\"pama_open_date\",\"key\":\"pama_open_date\",\"search\":\"\"}],\"column\":\"\",\"customParams\":{\"key\":\"RcZt\"}}",
    "end_time":1479052800000,
    "event_id":"",
    "modify_um":"梨花",
    "start_time":1479052800000,
    "temp_id":1,
    "update_time":1479102663000,
    "weight":"100",
    "ad_item":"[{\"column_name\":\"title\",\"column\":\"标题\",\"action\":1,\"$$hashKey\":\"object:1123\",\"value\":\"qu\"},{\"column_name\":\"content\",\"column\":\"文本内容\",\"action\":1,\"$$hashKey\":\"object:1124\",\"value\":\"fan\"},{\"column_name\":\"jump_url\",\"column\":\"跳转地址\",\"action\":1,\"$$hashKey\":\"object:1125\",\"value\":\"min\"}]"
}

url='http://10.25.166.117:8080/rmd/private/v1/ad/add'
headers = {'Content-Type': 'application/json'}
print data,type(json.dumps(data)),json.dumps(data)
print headers,type(json.dumps(headers)),json.dumps(headers)
request = urllib2.Request(url, headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request).read()
print response
'''
#   http://www.01happy.com/python-httplib-get-and-post/
'''
httpClient = None
try:
    httpClient = httplib.HTTPConnection('10.25.163.36', 80, timeout=30)
    httpClient.request('GET', '/push/ui/v1/sms/template/list?key=风险测评过期通知短信')

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
'''
'''
#post请求
httpClient = None
try:
    params = urllib.urlencode({
  "userId":"189608551",
  "code":"002639.SZ",
  "gainsPrice":8,
  "gainsRatio":0.02,
  "dropPrice":25,
  "dropRatio":0.01
})
    headers = {"Content-type":"application/json","Accept": "text/plain"}

    httpClient = httplib.HTTPConnection("10.25.164.108", 8080, timeout=30)
    httpClient.request("POST", "/ipush/private/v1/rule/warn", params, headers)

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
'''

'''
url = 'http://10.25.163.36/push/ui/v1/sms/send?appkey=SMS_TEST'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#values = {'name' : 'who','password':'123456'}
headers = { "Content-type":"application/json;charset=UTF-8"}
data = urllib.urlencode(data_json)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
'''