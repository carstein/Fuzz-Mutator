#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

# Local imports
import mutator
import transformations as trns


def main():
    m1 = mutator.EmptyMutator()
    m1.register_transformation(trns.add_sql_comments)
    m1.register_transformation(trns.random_case_swap)
    
    m1.load_fuzz("list.fz")
    
    m1.mutate()
    
#    print m1.pop_mutant(),
#    print m1.pop_mutant(),
#    print m1.pop_mutant(),
     
    for f in m1.pop_mutant():
        print f,

if __name__ == "__main__":
	sys.exit(main())
