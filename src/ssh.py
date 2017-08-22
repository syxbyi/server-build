#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'syxbyi'
__version__ = '1.0.0'

import subprocess
try:
    import utils
except:
    from . import utils

def main(distribution):
    utils.run_script(__file__, distribution)
    keygen = 'ssh-keygen'
    subprocess.call(keygen, shell = True)
    return

if __name__ == '__main__':
    distribution = 'ubuntu'
    main(distribution)

