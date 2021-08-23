# -*- coding:utf-8 -*-

from lib.io import shellAccept
from scan import get_plugins
from scan import run_plugins

if __name__ == "__main__":
    plugin_list = get_plugins()     # load plugins

    args = shellAccept()            # get shell data

    run_plugins(args.url, args.host, args.port, plugin_list)    # run plugins


