# -*- coding:utf-8 -*-

import argparse

def MyPrint(order, leakName):
    '''

    @param order: 说明测试情况，1表示漏洞存在，0表示漏洞不存在，-1表示产生异常
    @param leakName: 测试漏洞名称
    @return: None
    '''

    if order == -1:
        print("[-][scan generate error]----------" + leakName)
    elif order == 0:
        print("[-][leak not exist]----------" + leakName)
    elif order == 1:
        print("[+][leak exist]----------" + leakName)
    else:
        print("传递的漏洞标识数不在指定范围内，请修改")


def shellAccept():
    '''
    预定义命令行参数，接收并存储
    必须参数：None
    可选参数：
    -u / --URL
    -t / --threads
    -v / --version
    @return:返回获取到的命令行参数args，以数据字典格式
    '''
    try:    # 异常处理
        parser = argparse.ArgumentParser(description="传入命令参数")
        parser.add_argument("-U", "--url", type=str, help="待测试的URL", default="")
        parser.add_argument("-T", "--threads", type=str, help="线程数")
        parser.add_argument("-V", "--version", type=str, help="工具版本号")
        parser.add_argument("-H", "--host", type=str, help="ip地址", default="")  # 不能使用-h，-h已经被用来查看说明。可以用H
        parser.add_argument("-P", "--port", type=str, help="端口", default="")
        args = parser.parse_args()  # 获取参数字典
        return args
    except exception as e:
        print(e)








