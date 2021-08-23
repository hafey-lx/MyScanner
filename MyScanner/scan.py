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