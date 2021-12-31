#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2021/12/17 11:43
# @Author : ZhangTy
# @File : test2.py
import traceback
from pprint import pprint
# import logging
#
# # 默认输出等级为debug
# # logging.basicConfig(level="DEBUG")
#
# # 1.创建日志器
# log = logging.getLogger()
# # log.setLevel(level="DEBUG")
#
# # 2.创建处理器 处理日志输出的位置
#
# # 输出控制台
# console_handle = logging.StreamHandler()
# # 文本处理器,生成日志文件
# file_handle = logging.FileHandler("./log.txt", encoding="utf-8", mode="a")
# # 日志器要添加处理器 addHandler把输出内容添加进去
# log.addHandler(file_handle)
# log.addHandler(console_handle)
#
# log.debug("This is a debug log")
# log.info("This is a info log")
# log.warning("This is a warning log")
# log.error("This is a error log")
# log.critical("This is a critical log")
from common.Assert import log


class BaseAssert:
    @classmethod  # 使用类名就可以直接调用类方法
    def define_assert(cls, res, respData):
        try:
            if 'code' in respData:
                assert res['code'] == respData['code']
            elif 'msg' in respData:
                assert res['msg'] == respData['msg']
            else:
                assert res.get('error') == respData['error']
        except Exception as error:
            log.error(traceback.format_exc())
            raise error