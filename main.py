#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import getopt


def print_help():
    print(
    """Usage: ./main.py -f input [-o output] [-m mutator] [-h] 
    -h              - print this help 
    -f input        - mutate strings from this file
    -o output       - save results in a output file
    -m mutator      - use specified mutator"""
    )
    sys.exit(0)

def mutate(config):
    if config['mutator'] == '':
        config['mutator'] = "BasicMutator"
    
    try:
        mutator_module = __import__("laboratory.%s" % config['mutator'], fromlist=["laboratory"])
        mutator = mutator_module.Mutator()
    except ImportError:
        print("Could not find mutator: %s"%config['mutator'])
    except NotImplementedError:
        print("Could not make mutator from a mutatorFrame class")
   
    if config['input_file'] == "":
        print("No input file provided")
        print_help()
    
    try:
        mutator.load_fuzz(config['input_file'])
    except IOError:
        print("File %s not found"%config['input_file'])
        sys.exit(1)
    
    mutator.generate_results()
    
    if config['output_file'] != '':
        mutator.save_results(config[output_file])
    else:
        mutator.print_results()  

def main():
    configuration=  {
                    'input_file':'',
                    'output_file':'',
                    'mutator':'',
                    }
                    
    short_options = "hf:o:m:"
    long_options = ['help','file=','output=','mutator=']
    
    try:
        opt,args=getopt.getopt(sys.argv[1:],short_options,long_options)
    except:
        print_help()

    for o, ext in opt:
        if o in ("-h","--help"):
            print_help()
        if o in ("-f","--file"):
            configuration['input_file'] = ext
        if o in ("-m","--mutator"):
            configuration['mutator'] = ext
        if o in ("-o","--output"):
            configuration['output'] = ext
    
    mutate(configuration)
    
if __name__ == "__main__":
	sys.exit(main())
