#!/usr/bin/env python3

# -*- coding: utf8 -*-

import argparse
import os

def read_arg(args):
    """ Read cli argument and check if content the good value """
    
    parser = __create_parser()

    arg = vars(parser.parse_args())

    if arg["unicorn"]:
        __unicorn()
    
    return arg


def __create_parser():
    """ Create the parser of argument """
    
    parser = argparse.ArgumentParser(prog="adt_project")

    parser.add_argument("-i", "--input", type=__isdir, required=True,
                        help="directory content one dir per month.")
    parser.add_argument("-o", "--output", type=str, required=True,
                        help="prefix of all output file")

    # easter egg
    parser.add_argument("--unicorn", action='store_true',
                        help=argparse.SUPPRESS)
    
    return parser
    
    
def __isdir(val):
    val = str(val)

    if not os.path.isdir(val):
        raise argparse.ArgumentTypeError("We need "+val+" is a directory")

    return val

def __unicorn():
    print('\e[92m')
    print('\e[105m')
