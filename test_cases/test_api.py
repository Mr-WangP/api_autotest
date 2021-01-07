# coding=utf-8
import unittest
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.operation_header import OperationHeader
from util.operation_json import OperationJson


class RunTest(unittest.TestCase):

    def setUp(self) -> None:
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    def test_case(self):
        pass_count = []
        fail_count = []
        skip_count = []
        res = None
        # 获取用例数
        rows_count = self.data.get_case_lines()
        # 第一行索引为0
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                # request_data = self.data.get_request_data(i)
                # request_data = json.loads(request_data)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)

                if depend_case is not None:
                    depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    # 更新请求字段
                    request_data[depend_key] = depend_response_data
                # 如果header字段值为write则将该接口的返回的token写入到token.json文件，如果为yes则读取token.json文件
                if header == "write":
                    res = self.run_method.run_main(method, url, request_data)
                    op_header = OperationHeader(res)
                    op_header.write_token()
                elif header == 'yes':
                    op_json = OperationJson("../dataconfig/token.json")
                    token = op_json.get_data('data')
                    request_data = dict(request_data, **token)  # 把请求数据与登录token合并，并作为请求数据

                    res = self.run_method.run_main(method, url, request_data)
                else:
                    res = self.run_method.run_main(method, url, request_data)

                if expect is not None:
                    if self.com_util.is_contain(expect, res):
                        self.data.write_result(i, res)
                        self.data.write_test_result(i, "Pass")
                        pass_count.append(i)
                    else:
                        self.data.write_result(i, res)
                        self.data.write_test_result(i, 'Fail')
                        fail_count.append(i)
                else:
                    print(f"用例ID：case-{i}，预期结果不能为空")
            else:
                self.data.write_test_result(i, "Skip")
                skip_count.append(i)

        print(f"通过用例数：{len(pass_count)}")
        print(f"失败用例数：{len(fail_count)}")
        print(f"跳过用例数：{len(skip_count)}")


if __name__ == '__main__':
    unittest.main()
