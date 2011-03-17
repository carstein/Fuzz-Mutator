#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import string

def empty_encode(str):
    """No encoding"""
    t0=str
    tn=t0
    return str

def uri_encode(str):
    """Do the URI encoding"""
    t0=str
    t1=""
    for c in (t0[:-1]):
        t1+="%"+hex(ord(c))[2:]
    t1+="\n"    
    tn=t1
    return tn

def double_uri_encode(str):
    """Do the double URI encoding"""
    t0=str
    t1=""
    for c in (t0[:-1]):
        t1+="%25"+hex(ord(c))[2:]
    t1+="\n"    
    tn=t1
    return tn
