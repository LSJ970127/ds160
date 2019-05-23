# -*- coding: utf-8 -*-
"""
@author: ZhaoBin
@file: settings.py 
Created on 2018/5/5 16:44
"""
import json
import os
import sys
from time import sleep, strftime, time, strptime, mktime

import pymysql
from DBUtils.PooledDB import PooledDB

try:
    with open("veri.json") as f:
        pass
except Exception:
    with open("veri.json", "w") as f:
        pass

NC = 'noClick'

# BASEDIR = "F:\\usFile"
BASEDIR = "C:\\Users\\Administrator\\Desktop\\automation_us"
USFILE = "D:\\usfile"
if not os.path.isdir(USFILE):
    os.makedirs(USFILE)

LogDir = ".\\us_log"
if not os.path.isdir(BASEDIR):
    os.mkdir(BASEDIR)
if not os.path.isdir(LogDir):
    os.mkdir(LogDir)


PD_ID   = "108534"
PD_KEY  = "XLEQruFUk1cqp/i7blRc5qH8JhWfEm93"
APP_ID  = "308532"
APP_KEY = "QtUAXB6ust+uJm5cW2qLwA/RR1VlEA0F"
FATEA_PRED_URL  = "http://pred.fateadm.com"

USER = "csy518@icloud.com"
USERPHOTO = "18801235888"
USERDB = "mobtop"
PASSWD = "5678tyui"

# 数据库（MySQL）连接数据
DBHOST = '60.205.119.77'
DBUSER = 'mobtop'
DBPWD = 'DLtx5t6y7u8i'
DBNAME = 'mobtop'
DBPORT = 3306
DBCHAR = "utf8mb4"

# douxin7
# DBUSER = 'haoyunyun'
# DBPWD = 'C5t6y7u8iC'
# DBNAME = 'douxin7'

LOGOAPI_URL = "https://www.mobtop.com.cn/index.php?s=/Business/Pcapi/insertlogoapi"

MONTH = {
    "01": "JAN",
    "02": "FEB",
    "03": "MAR",
    "04": "APR",
    "05": "MAY",
    "06": "JUN",
    "07": "JUL",
    "08": "AUG",
    "09": "SEP",
    "10": "OCT",
    "11": "NOV",
    "12": "DEC",
}
MON = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
MON_ANTI = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12",
}


APPDAYS = ["07", "08", "09", "10", "11", "13", "14", "15", "16"]


# def POOL():
#     return PooledDB(
#         pymysql,
#         mincached=1,
#         maxcached=3,
#         maxconnections=5,
#         host='60.205.119.77',
#         user="mobtop",
#         passwd='CSY5t6y7u8iC',
#         db="mobtop",
#         port=3306,
#         cursorclass=pymysql.cursors.DictCursor,
#         charset="utf8"
#     )


class UsError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo
        self._log()

    def _log(self):
        with open(f'us_log/{strftime("%Y%m%d")}.log', 'a', encoding='utf8') as f:
            text = f"{strftime('%Y-%m-%d %H:%M:%S')}\t" + \
                self.errorinfo + '\n\n'
            f.write(text)

    def __str__(self):
        return self.errorinfo


# BROKER_URL = 'amqp://root:123456@192.168.0.158:5672'
# BROKER_URL = 'redis://:5678tyui@localhost:6379/0'
BROKER_URL = 'redis://:5678tyui@182.92.69.238:6379/0'

# 可见性超时
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 1 hour.

# 广播信息默认队所有虚拟主机可见
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True}

# 如果你也想在 Redis 中存储任务的状态和返回值，你应该配置这些选项
# CELERY_RESULT_BACKEND = 'redis://:5678tyui@localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://:5678tyui@182.92.69.238:6379/0'
# CELERY_RESULT_BACKEND = 'amqp://root:123456@192.168.0.158:5672'
