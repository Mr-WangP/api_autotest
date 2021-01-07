# coding=utf-8
import json
from util.operation_json import OperationJson
from base.runmethod import RunMethod


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_token(self):
        """
        获取登录返回的token
        """
        token = {"data": {"token": self.response['data']['token']}}
        return token

    def write_token(self):
        op_json = OperationJson()
        op_json.write_data(self.get_response_token())


if __name__ == '__main__':
    url = "http://xxxxx"

    data = {
        "username": "1111",
        "password": "123456"
    }
    run_method = RunMethod()
    # res = json.dumps(requests.post(url, data).json())
    res = run_method.run_main('Post', url, data)
    op = OperationHeader(res)
    op.write_token()
