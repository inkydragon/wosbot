#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.mirai import Bot as MIRAIBot


# Custom your logger
# 
from nonebot.log import logger, default_format
logger.add("./log/error.log",
           rotation="00:00",
           diagnose=False,
           level="ERROR",
           format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("mirai", MIRAIBot)

nonebot.load_builtin_plugins()  # 加载 nonebot 内置插件
nonebot.load_plugins("src/plugins")
nonebot.load_plugin("nonebot_plugin_test")
# nonebot.load_plugin("nonebot_plugin_status")
# nonebot.load_plugin("haruka_bot")
nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app",
                reload_exclude_dirs=['bin', 'log', 'data', '__pycache__'])
