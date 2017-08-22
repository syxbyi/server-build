#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'syxbyi'
__version__ = '1.0.0'

import subprocess
from os.path import join, dirname, basename, splitext
import sys

def ask(string):
    if not '[y/n]' in string.lower():
        string += ' [Y/n]: '
    if sys.version_info[0] < 3:
        answer = raw_input(string)
    else:
        answer = input(string)
    if answer in ['y', 'yes', 'Y']:
        return True
    else:
        return False

def get_dir(filename):
    directory = join(dirname(__file__), splitext(basename(filename))[0])
    return directory

def get_src(filename, distribution):
    directory = get_dir(filename)
    src = join(directory, '%s.sh' % distribution)
    return src

def run_script(filename, distribution):
    src = get_src(filename, distribution)
    subprocess.call('bash "%s"' % src, shell = True) 
    return

def main():
    return

if __name__ == '__main__':
    main()
