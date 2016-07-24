#!/usr/bin/env python
# encoding: utf-8


RE_DB = 'time=(\d{1,10})\|.*?sql=\"select.*? from (flow\_.*?) .*?'
RE_API ='\|(\/bmis\/v1_0.*?)\|(\d{1,10})\|'
DIR_LOG ='/Users/Michael/0.flow.log'
POINTS_X_GET_ORDER_COUNT = 1
POINTS_X_GET_GROUP_NAME = 2
