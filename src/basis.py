#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'syxbyi'
__version__ = '1.0.0'

from . import utils

def main(distribution):
    utils.run_script(__file__, distribution)
    return

if __name__ == '__main__':
    distribution = 'ubuntu'
    main(distribution)

