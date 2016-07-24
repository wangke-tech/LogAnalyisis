#!/usr/bin/env python
# encoding: utf-8

import os
import sys

"""
print 'os.path.dirname(__file__):'
print os.path.abspath(__file__),'\n'
print 'os.path.dirname(os.path.abspath(__file__)):'
print os.path.dirname(os.path.abspath(__file__)),'\n'
print 'nos.path.dirname(os.path.dirname(os.path.abspath(__file__))):'
print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""

HOME = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'bin')
DOCUMENT_ROOT = HOME
