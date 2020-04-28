import requests
import logging


# 不保存Cookie
class RequestsHandler:

    def get(self, url, params=None, **kw):
        """发送get请求"""
        try:
            res = requests.get(url, params=params, **kw)
        except:
            # 抛出异常
            logging.error("访问不成功")
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """发送post请求"""
        try:
            res = requests.post(url, data=data, json=json, **kw)
        except:
            # 抛出异常
            logging.error("访问不成功")
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口"""
        if method.lower() == 'get':
            return self.get(url, params=params, **kw)
        elif method.lower() == 'post':
            return self.post(url, params=params, data=data, json=json, **kw)
        else:
            return requests.request(method, url, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """获取json数据"""
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error("不是json格式的数据")
            return res.text


# 保存Cookie
class RequestCookiesHandler:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, **kw):
        """发送get请求"""
        try:
            res = self.session.get(url, params=params, **kw)
        except:
            # 抛出异常
            logging.error("访问不成功")
        else:
            return res

    def post(self, url, data=None, json=None, **kw):
        """发送post请求"""
        try:
            res = self.session.post(url, data=data, json=json, **kw)
        except:
            # 抛出异常
            logging.error("访问不成功")
        else:
            return res

    def visit(self, method, url, params=None, data=None, json=None, **kw):
        """访问接口"""
        if method.lower() == 'get':
            return self.get(url, params=params, **kw)
        elif method.lower() == 'post':
            return self.post(url, params=params, data=data, json=json, **kw)
        else:
            return self.session.request(method, url, **kw)

    def json(self, method, url, params=None, data=None, json=None, **kw):
        """获取json数据"""
        res = self.visit(method, url, params=params, data=data, json=json, **kw)
        # 获取json数据
        try:
            return res.json()
        except:
            # 记录日志信息
            logging.error("不是json格式的数据")
            return res.text
