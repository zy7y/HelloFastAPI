# https://github.com/CoderCharm/MallAPI/blob/master/app/extensions/logger.py
import os
import time

from loguru import logger

basedir = os.path.dirname(os.path.abspath(__file__))

# 定位到log日志文件
log_path = os.path.join(basedir, '../logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

# 日志简单配置
logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)


__all__ = ["logger"]

