# coding=utf-8
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
# from util.send_mail import SendMail
from util.log import LOG


def run():

    LOG().log('log').info("开始执行！")
    # 指定测试用例为当前文件夹下的 test_cases 目录
    test_dir = './test_cases'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    file_path = './report/' + now_time + '_result.html'
    fp = open(file_path, mode='wb')
    runner = HTMLTestRunner(stream=fp, title='接口自动化测试报告', description="运行环境：requests, unittest")
    runner.run(suit)
    fp.close()

    LOG().log('log').info("运行结束，生成测试报告！")
    # 发送邮件
    # send_email = SendMail()
    # send_email.send_mail(file_path)


if __name__ == '__main__':
    run()
