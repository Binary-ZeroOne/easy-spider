from urllib import request

import http.cookiejar

url = "https://www.baidu.com"

print('第一种通过urllib获取网页内容的方法')
response_one = request.urlopen(url)
# 得到http状态码以及网页内容的长度
print(response_one.getcode())
print(len(response_one.read()))

##########################################################

print('\n第二种通过urllib获取网页内容的方法')
# 添加http的请求头信息
request_one = request.Request(url)
request_one.add_header("user-agent", "Mozilla/5.0")
response_two = request.urlopen(request_one)
print(response_two.getcode())
print(len(response_two.read()))

##########################################################

print('\n第三种通过urllib获取网页内容的方法')
# 增加cookie处理
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response_three = request.urlopen(url)
print(response_three.getcode())
print(cj)

data = response_three.read()
print(data)
print(len(data))
