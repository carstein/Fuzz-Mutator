#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import string
import itertools


class MutatorFrame(object):
    # TODO - add protection agains making an instance of this class
    
    t_list=[]
    fuzz_lines=[]
    e_list=[]
    output=[]
    
    def register_transformation(self,t):
        self.t_list.append(t)
      
    def register_encoder(self,e):
        self.e_list.append(e)
    
    def load_fuzz(self, filename):
        try:
            fh = open(filename, "r")
            self.fuzz_lines = fh.readlines()
            fh.close()
        except IOError:
            print("File %s not found"%filename)
            sys.exit(1)
          
    def combine_mutations(self):
        combination_gen=itertools.permutations(self.t_list,len(self.t_list))
        for c in combination_gen:
            yield c
            
    def mutate(self):
        output = self.fuzz_lines

        for ts in self.combine_mutations():
            for t in ts:
                output=map(t,output)    
            yield output
    
    def save_list(self,filename):
        try:
            fh=open(filename,"w+")
            fh.write(string.join(self.output,""))
            fh.close()
        except IOError:
            print("Could not write to file: %s"%filename)
            sys.exit(1)
    
    def generate_results(self):
        for ms in self.mutate():
            for m in ms: 
                self.output.append(m)
            
        self.encode()
        
    def print_results(self):
        for line in self.output:
            print line,
     
    def encode(self):
        for e in self.e_list:
            self.output=map(e,self.output)
    
    def reduce(self):
        seen = {} 
        output = []
        
        for item in self.output:
            if item in seen: continue 
            seen[item] = 1 
            result.append(item) 
        
        self.output = result
