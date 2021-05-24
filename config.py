
import os

PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(PRO_PATH, "test_cases", "")

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 选择测试数据文件
    file_path = os.path.join(PRO_PATH, "data", "case.xlsx")
    # 选择测试数据文件的表单
    sheet_id = 0
    # 选择接口请求的token文件
    token_file = os.path.join(PRO_PATH, "data", "token.json")
