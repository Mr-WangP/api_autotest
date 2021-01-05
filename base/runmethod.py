# coding=utf-8
import json
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header is not None:
            urllib3.disable_warnings()
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            urllib3.disable_warnings()
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            urllib3.disable_warnings()
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            urllib3.disable_warnings()
            res = requests.get(url=url, params=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        elif method == 'get':
            res = self.get_main(url, data, header)
        else:
            print('只支持post/get方法')
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    data = {
        'cart': '11'
    }
    run = RunMethod()
    run_test = run.run_main(method="Post", url=url, data=data)
    print(run_test)
