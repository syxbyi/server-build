#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Run in root
'''

__author__ = 'syxbyi'
__version__ = '1.0.0'

from os.path import join, dirname
import os
import subprocess
from argparse import ArgumentParser
from configparser import ConfigParser
try:
    from . import utils
except:
    import utils
try:
    from . import conf_spark
except:
    import conf_spark

class Sparker(object):
    def __init__(self):
        self.dst = None         # spark install destination
        self.profile = None     # spark config profile
        self.do = True          # do install and config spark
        self.pc = False         # install spark without cluster config
        self._parse()
        if not self.do:
            return
        if not os.path.isdir(self.dst):
            os.makedirs(self.dst)

    # read config, read options, set self variables and ask for comfirm
    def _parse(self):
        arg_parser = ArgumentParser()
        arg_parser.add_argument('-p', '--pc', help = 'Install spark on your pc (not server machine)', action = 'store_true')
        arg_parser.add_argument('-f', '--file', help = 'Specify spark src pkg here')
        # options in group cannot be use together
        group = arg_parser.add_mutually_exclusive_group()
        group.add_argument('--ubuntu', help = 'Install spark for ubuntu', action = 'store_true')
        group.add_argument('--fedora', help = 'Install spark for fedora', action = 'store_true')
        args = arg_parser.parse_args()
        if args.ubuntu:
            self.distribution = 'ubuntu'
        elif args.fedora:
            self.distribution = 'fedora'
        cfg_parser = ConfigParser()
        src_dir = utils.get_dir(__file__)
        cfg_parser.read(join(src_dir, 'config.ini'))
        # set spark home and target profile
        if args.pc:
            self.pc = True
            home = os.environ['HOME']
            self.dst = join(home, cfg_parser.get('pc', 'dst'))
            self.profile = join(home, cfg_parser.get('pc', 'profile'))
        else:
            self.pc = False
            self.dst = cfg_parser.get('server', 'dst')
            self.profile = cfg_parser.get('server', 'profile')
        # spark src pkg
        self.version = cfg_parser.get('src', 'src')
        if args.file:
            self.src = args.file
        else:
            self.src = join(src_dir, self.version)
        if not os.path.isdir(self.src):
            print('!!! Cannot locate spark src pkg. Please check README file.')
            self.do = False
            return
        # get spark env info to write to profile
        self.env = join(src_dir, cfg_parser.get('src', 'profile'))
        string = 'Install spark in %s and config spark in profile %s?\nSpark source will be got in %s. And file %s will be wrote to profile\n' % (self.dst, self.profile, self.src, self.env)
        if not utils.ask(string):
            self.do = False

    def run_script(self, distribution = None):
        if not self.do:
            return
        print('--- installing dependencies')
        if self.distribution:
            distribution = self.distribution
        elif not distribution:
            exit('!!! No distribution name has been given.')
        utils.run_script(__file__, distribution)
        return

    # decompress and install
    def install(self):
        if not self.do:
            return
        print('--- copy spark files to %s' % self.dst)
        cp = 'cp -R "%s" "%s"' % (self.src, self.dst)
        subprocess.call(cp, shell = True)
        print('--- success')
        return

    # write spark env to profile
    def config(self):
        if not self.do:
            return
        print('--- checking spark environments')
        with open(self.profile, 'r') as dst:
            content = str(dst.read())
        if not 'SPARK_HOME' in content:
            with open(self.env, 'r') as src, open(self.profile, 'a') as dst:
                print('--- writing spark environments to profile')
                for line in src:
                    if 'SPARK_HOME=' in line:
                        line = line.replace('=', '="%s"' % join(self.dst, self.version))
                    dst.write(line)
        if not self.pc:
            conf_spark.main(self.profile)
        print('--- ok')

def main(distribution = None):
    # add distribution functions
    sparker = Sparker()
    sparker.run_script(distribution)
    sparker.install()
    sparker.config()
    return

if __name__ == '__main__':
    main()
