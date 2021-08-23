## 前言

由于SQLMap、Pocsuite3等开源漏洞扫描器的功能较多，尝试静态代码审计 + 动态代码审计，虽然有些许收获，但盲人摸象的学习方式对个人架构能力的益处甚少。因此考虑自己动手梳理和编写漏洞扫描器，通过不断地对比和完善来进行学习。

漏洞扫描器：使用插件技术，对主机漏洞 / Web漏洞进行探测。

插件是指 **脚本语言编写的子程序** ，通常系统先制定扫描策略，然后扫描程序根据策略调用一系列插件来执行漏洞扫描 ，检测出系统中存在的一个或多个漏洞。

编程语言：Python3。

## Demo需求分析

#### 用户界面
用户界面，采用命令行模式。

Demo的命令参数如下，Demo阶段不认为用户体验应当成为重要部分。
| 需求         | 指定参数        |
| ------------ | --------------- |
| 指定扫描目标 | -u和-f url_file |
| 设置线程数   | --threads       |
| 获取参数帮助 | -h              |
| 获取版本信息 | -v              |

参数问题1：需要指定端口号吗？待议。

命令行模式主要需要考虑2个问题：命令行的参数接收；接收后根据不同的参数调用不同的功能。（参数是否存储待议）

统一的输出格式：Demo阶段定义一个函数即可。

#### 插件目录plugins
Poc数量：考虑放置3个Poc，用于Demo测试。

加载插件的方式？

统一调用插件：需要在各个插件里封装统一的扫描函数。

访问对象问题1：是否需要统一设置访问对象，比如cookie、headers等？内网扫描需要该功能，外网扫描不需要，Demo阶段不设置统一访问对象。


#### 数据的存储和传输

像SQLMap、Pocsuite3都设置了比较巧妙的自定义字典，提出问题1：为什么要设置自定义字典，直接使用变量进行存储不行吗？

场景：main文件出现变量的话会显得比较混乱，所以我们默契达成约定，main文件中只会调用封装的函数，不会出现什么变量。（当然可以在main文件中定义接收和处理变量的函数）

问题2：比如我们设置了一个接收和处理变量的函数，那么它如何传递给main函数，main函数又如何传递给其他函数？

思路1：可以尝试函数返回一个字典给main函数，通过这个字典进行usage的传输和设置。（可以尝试）




## 文件准备
#### 作图表示
创建目录和py文件，Demo的树状图结构如下。![在这里插入图片描述](https://img-blog.csdnimg.cn/fb1f891afd874a25ac58488f9079f817.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NvbGRpX2Vy,size_16,color_FFFFFF,t_70)


#### 编写io处理代码
###### io.py的输出函数MyPrint(order, leakName)
```'
# -*- coding:utf-8 -*-

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
```

###### io.py的命令行参数处理函数xxx
编写过程
```'
import argparse
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
        parser.add_argument("-u", "--URL", type=str, help="待测试的URL")
        parser.add_argument("-t", "--threads", type=str, help="线程数")
        parser.add_argument("-v", "--version", type=str, help="工具版本号")
        args = parser.parse_args()  # 获取参数字典
        return args
    except exception as e:
        print(e)

```

#### 编写scan.py
```'
# -*- coding:utf-8 -*-

import os
import plugins

def get_plugins():
    result = []
    plugins_list = [f.split(".")[0] for f in os.listdir("plugins") if f.endswith(".py")]  # 加载所有插件

    for i in plugins_list:
        exec("import plugins." + i)  # 导入每个插件文件

    return plugins_list

def run_plugins(domain, ip, port, plugin_list):

    for plugins_name in plugin_list:
        eval("plugins." + plugins_name + ".scan('" + domain + "','" + ip + "','" + port + "')")
```
#### 准备插件：3个Poc脚本

###### 统一的scan()主函数
问题1：插件从何处接收 `目标URL` 信息？

方法一：统一scan(protol, domain, ip, port)，扫描器引擎通过遍历plugins目录获取所有文件名，然后执行命令 `eval("plugins." + filename + ".scan(protol, domain, ip, port)")` 进行扫描。

#### 引用报错

报错原因：使用相对路径进行引用导致的报错。

解决方法1：调整脚本目录， 代码 `import sys;sys.path.append("../")`
![在这里插入图片描述](https://img-blog.csdnimg.cn/bd63762ff1d84f48a8ef77e22d841b85.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NvbGRpX2Vy,size_16,color_FFFFFF,t_70)
## 编写main.py扫描器引擎

问题1：如何加载插件？见scan.py
```'
import plugins

def get_plugins():
    result = []
    plugins_list = [f.split(".")[0] for f in os.listdir("plugins") if f.endswith(".py")]  # 加载所有插件

    for i in plugins_list:
        exec("import plugins." + i)  # 导入每个插件文件

    return plugins_list
```
问题2：如何调用插件？见scan.py
```'
def run_plugins(plugins_name, domain, ip, port):

    eval("plugins." + plugins_name + ".scan('" + scheme + "','" + domain + "','" + ip + "','" + port + "')")
```
问题3：接收用户输入，进行异常处理，传递URL数据。见io.py。

主文件main.py代码：
```'
# -*- coding:utf-8 -*-

from lib.io import shellAccept
from scan import get_plugins
from scan import run_plugins

if __name__ == "__main__":
    plugin_list = get_plugins()     # load plugins

    args = shellAccept()            # get shell data

    run_plugins(args.url, args.host, args.port, plugin_list)    # run plugins
```

程序运行效果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/f5ff167310ef4898868e1738b418ea93.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NvbGRpX2Vy,size_16,color_FFFFFF,t_70)

