#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import string

class EmptyMutator:
    def __init__(self, t_list=[],fuzz_lines=[]):
        self.t_list=t_list
        self.fuzz_lines=fuzz_lines
        self.output=[]
    
    def register_transformation(self,t):
        self.t_list.append(t)
    
    def load_fuzz(self, filename):
        fh = open(filename, "r")
        self.fuzz_lines = fh.readlines()
        fh.close()
        
    def mutate(self):
        self.output = list(self.fuzz_lines)
        for t in self.t_list:
            self.output=map(t,self.output)
               
    def pop_mutant(self):
        mutant=self.output.pop()
        yield mutant
        
    def save_list(self,filename):
        fh=open(filename,"w+")
        fh.write(string.join(self.output,""))
        fh.close()
