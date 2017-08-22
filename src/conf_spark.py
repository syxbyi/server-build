#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'syxbyi'
__version__ = '1.0.0'

from os.path import join
import os
import shutil
try:
    from . import utils
except:
    import utils

def add(src, dst):
    print('--- Add file content from %s to %s' % (src, dst))
    with open(dst, 'a') as d, open(src, 'r') as s:
        d.write(s.read())

def spark_conf(src, dst):
    # configure spark need copy template file to conf file
    if not os.path.isfile(dst):
        print('--- Copy template file')
        shutil.copy('%s.template' % dst, dst)
    add(src, dst)

def main(profile = None):
    src = utils.get_dir(__file__)
    # add hosts file
    shosts = join(src, 'hosts')
    dhosts = '/etc/hosts'
    #add(shosts, dhosts)
    # find spark path
    try:
        sparkconf = None
        sparkconf = join(os.environ['SPARK_HOME'], 'conf')
    except KeyError:
        # try to find spark home from profile
        if not profile:
            print('!!! There is no SPARK_HOME variable, please check your spark installation or try to restart your terminal, or specify a profile.')
            return
        with open(profile, 'r') as f:
            for line in f:
                if 'SPARK_HOME=' in line:
                    # cut the string with the first " and the last ", get the path between them.
                    sparkhome = line[line.find('"') + 1 : line.rfind('"')]
                    print(sparkhome)
                    sparkconf = join(sparkhome, 'conf')
                    break
        if not sparkconf:
            print('!!! Profile error, your profile does not contain SPARK_HOME variable. The path for SPARK_HOME should be enclosed by "')
            return
    # conf spark slaves
    sslaves = join(src, 'slaves')
    dslaves = join(sparkconf, 'slaves')
    spark_conf(sslaves, dslaves)
    # conf spark env
    sspark_env = join(src, 'spark-env.sh')
    dspark_env = join(sparkconf, 'spark-env.sh')
    spark_conf(sspark_env, dspark_env)
    return

if __name__ == '__main__':
    profile = '/home/syxbyi/.bashrc'
    main(profile)
