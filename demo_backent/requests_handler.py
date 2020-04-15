import requests
import logging


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
