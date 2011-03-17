#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import string

def add_sql_comments(str):
	"""Insert comments into SQL command"""
	t0=str
	
	t1=t0.replace(" ","/**/")
	t2=t1.replace("=","/**/=")
	
	tn=t2
	
	return tn

def random_case_swap(str):
    """Randomly swap cases from uppercase to lowercase and vice versa in a string"""
    
    t0=str
    t1=""
    
    for c in t0:
        if (c in string.letters) and (random.randint(1,10)>5):
            t1+=c.swapcase()
        else:
            t1+=c
                
    tn=t1
    
    return tn
