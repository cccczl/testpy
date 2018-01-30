#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;

ticks = time.time()
print "当前时间戳：", ticks

localtime = time.asctime(time.localtime())
print "本地时间：", localtime