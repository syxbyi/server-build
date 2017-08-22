#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'syxbyi'
__version__ = '1.0.0'

from os.path import join, dirname
import subprocess
from . import utils

def pip_install():
    requirements = join(get_dir(__file__), 'requirements.txt')
    pip = 'pip install -r %s' % requirements
    subprocess.call(pip, shell = True)
    return

def main(distribution):
    utils.run_script(__file__, distribution)
    pip_install()
    return

if __name__ == '__main__':
    distribution = 'ubuntu'
    main(distribution)

