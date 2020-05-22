# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import you_get
import os

'''
-O 文件名
-o 文件保存路径
--debug debug日志
'''


def download(url, filename):
    try:
        info = os.system(r'you-get --debug -O {} -o /root  {}'.format(filename, url))
        print(info)
    except Exception as e:
        print(e)


'''
视频地址 https://www.bilibili.com/video/av38608415/?p=34

demo: python down.py  https://www.bilibili.com/video/av38608415 34
'''
if __name__ == '__main__':
    # 视频网站的地址
    base_url = "https://www.bilibili.com/video/av38608415"  # 视频地址
    nums = 34  # 34页
    nums = int(nums)
    for p in range(1, nums):
        url = base_url + "/?p=" + str(p)
        download(url, p)
