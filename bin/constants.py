#!/usr/bin/env python
# encoding: utf-8


DIR_LOG ='/Users/Michael/0.flow.log'

RE_DB = 'time=(\d{1,10})\|.*?sql=\"select.*? from (flow\_.*?) .*?'
RE_API ='\|(\/bmis\/v1_0.*?)\|(\d{1,10})\|'
"""
STR_API_GET_ORDER_COUNT = '/bmis/v1_0/order/getOrderCount'
STR_API_GET_GROUP_NAME = '/bmis/v1_0/user/getGroupName'
STR_API_GET_ORDER_LIST_DURATION = '/bmis/v1_0/order/getOrderListDuration'
STR_API_GET_ORDER_LIST_DETAIL = '/bmis/v1_0/order/getOrderDetail'

POINTS_X_GET_ORDER_COUNT = 1
POINTS_X_GET_GROUP_NAME = 2
POINTS_X_GET_ORDER_LIST_DURATION = 3
POINTS_X_GET_ORDER_LIST_DETAIL = 4
"""
