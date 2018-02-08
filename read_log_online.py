# -*- coding: utf-8 -*-
__author__ = "chenk"
import time

def read(file):
    with open(file) as f:
        while True:
            f_read = f.readline()
            if not f_read:
                time.sleep(0.5)
            else:
                print(f_read)


read(r"D:\iSeeRobotAdvisor\trunk\Documents\D3.Testing\大数据测试jmeter\apache-jmeter-3.2\bin\jmeter.log")