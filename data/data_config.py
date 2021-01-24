# coding=utf-8
class global_val:
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'
    test_result = '12'


def get_id():
    """获取case_id"""
    return global_val.Id


def get_request_name():
    """获取请求模块名称"""
    return global_val.request_name


def get_url():
    """获取请求url"""
    return global_val.url


def get_run():
    """获取是否运行"""
    return global_val.run


def get_run_way():
    """获取请求方式"""
    return global_val.request_way


def get_header():
    """获取是否携带header"""
    return global_val.header


def get_case_depend():
    """case依赖"""
    return global_val.case_depend


def get_data_depend():
    """依赖的返回数据"""
    return global_val.data_depend


def get_field_depend():
    """数据依赖字段"""
    return global_val.field_depend


def get_data():
    """获取请求数据"""
    return global_val.data


def get_expect():
    """获取预期结果"""
    return global_val.expect


def get_result():
    """获取返回结果"""
    return global_val.result


def get_test_result():
    """获取返回结果"""
    return global_val.test_result
