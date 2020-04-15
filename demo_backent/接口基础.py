import requests

# 发送http请求
proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
url = 'http://127.0.0.1:5000/login'
data = {"user": "yuz", "pwd": "1232456"}
res = requests.get(url, proxies=proxies, params=data)
print(res.text)
cookies = res.cookies

# 带请求头
# headers = {"Ur-Agent": "huawei p30"}
# # 传递参数的三种方式,params dasta json
# res = requests.get(url, proxies=proxies, params=data, headers=headers)

url1 = "http://127.0.0.1:5000/"
res1 = requests.post(url1, cookies=cookies)
print(res1.text)