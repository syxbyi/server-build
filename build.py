#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'syxbyi'
__version__ = '1.0.0'

from argparse import ArgumentParser
import src.basis
import src.python
import src.spark
import src.conf_spark

def parse():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', help = 'specify spark src file path', nargs = '+')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--ubuntu', help = 'Build for Ubuntu', action = 'store_true')
    group.add_argument('--fedora', help = 'Build for Fedora', action = 'store_true')
    args = parser.parse_args()
    if args.fedora:
        return 'fedora', args.file
    elif args.ubuntu:
        return 'ubuntu', args.file
    return None

def main():
    distribution, src = parse()
    src.basis.main(distribution)
    src.python.main(distribution)
    src.spark.main(distribution, src)
    return

if __name__ == '__main__':
    main()

