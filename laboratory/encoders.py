#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import string
import base64

def empty_encode(t0):
    """No encoding"""
    tn=t0
    return tn

def uri_encode(t0):
    """Do the URI encoding"""
    t1=""
    for c in (t0[:-1]):
        t1+="%"+hex(ord(c))[2:]
    t1+="\n"    
    tn=t1
    return tn

def double_uri_encode(t0):
    """Do the double URI encoding"""
    t1=""
    for c in (t0[:-1]):
        t1+="%25"+hex(ord(c))[2:]
    t1+="\n"    
    tn=t1
    return tn

def base64_encode(t0):
    """Do the base64 encode"""
    tn=base64.encodestring(t0)
    return tn

def php_string_escape_encode(t0):
    """Do the php string encode. Example: ABC -> chr(65).chr(66).chr(67)"""
    t1=""
    
    for c in t0[:-1]:
        t1+="chr(%d)."%ord(c)
        
    tn=t1[:-1]+"\n"
    return tn

def first_nibble_encode(t0):
    """Do the nibble encoding on the first parameter A -> %%341"""
    
    t2=""
    
    for c in t0[:-1]:
        t1=hex(ord(c))
        t2+="%%"+hex(ord(t1[-2]))[2:]+t1[-1]
        
    tn=t2+"\n"
    return tn
