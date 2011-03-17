#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import mutator
import transformations as trns
import encoders as enc


class Mutator(mutator.MutatorFrame):
    def __init__(self):
        # Load basic transformations and encoding
        self.register_transformation(trns.add_sql_comments)
        self.register_transformation(trns.random_case_swap)
        self.register_encoder(enc.empty_encode)
        self.register_encoder(enc.double_uri_encode)
