"""
请求方法类
"""
import requests


class General_request:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    # post请求方法
    def post_way(self, url, params=None, data=None, json=None, headers=None):
        result = self.session.post(url, params=params, data=data, json=json, headers=headers)
        try:
            # 返回json结果
            return result
        except Exception:
            return 'not json'

    # get请求方法
    def get_way(self, url, params=None, headers=None):
        result = self.session.post(url, params=params, headers=headers)
        try:
            # 返回json结果
            return result
        except Exception:
            return 'not json'

    def close_session(self):
        self.session.close()
