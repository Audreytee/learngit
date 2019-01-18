# 发送request请求：
# urlib
# from urllib import request
# requests模块，推荐
import requests

class HTTP:
    @staticmethod
    def get(url,return_json=True):
        r = requests.get(url)
        # restful要求返回json的数据
        # if和else很多会添加很多的思维分支，会混乱，最好及早简化。
        # 简化if和else
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     return r.text
        # else:
        #     if return_json:
        #         return {}
        #     return ''
    # 类方法
    @classmethod
    def get1(cls):
        pass

