#!/usr/bin/env python
# encoding: utf-8

import os
import sys
from common.base import loader
from flow_log import main as stats

HOME = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if '__main__' == __name__:

    # 配置路径
    if 1 > len(sys.argv):
        loader.loadconf(HOME, sys.argv[1])
    elif 1 == len(sys.argv):
        loader.loadconf(HOME)

    stats()

