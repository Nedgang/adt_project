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

    parser = argparse.ArgumentParser(prog="adt_project",
                                     formatter_class=
                                     argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--input", type=__isdir, required=True,
                        help="directory content one dir per month")
    parser.add_argument("-o", "--output", type=str, required=True,
                        help="prefix of all output file")
    parser.add_argument("-f", "--filter-dir", type=__isdir,
                        default="data/filtration/",
                        help="We read all file in this dir to filter word")

    
    # easter egg
    parser.add_argument("--unicorn", action='store_true',
                        help=argparse.SUPPRESS)

    return parser


def __isdir(val):
    val = str(val)

    if not os.path.isdir(val):
        raise argparse.ArgumentTypeError(val+" is not a directory")

    return val

def __unicorn():
    print('\033[92m')
    print('\033[105m')
    print('\033[1m')
    print("""
                                                    /
                                                  .7
                                       \       , //
                                       |\.--._/|//
                                      /\ ) ) ).'/
                                     /(  \  // /
                                    /(   J`((_/ \ 
                                   / ) | _\     /
                                  /|)  \  eJ    L
                                 |  \ L \   L   L
                                /  \  J  `. J   L
                                |  )   L   \/   \ 
                               /  \    J   (\   /
             _....___         |  \      \   \```
      ,.._.-'        '''--...-||\     -. \   \ 
    .'.=.'                    `         `.\ [ Y
   /   /                                  \]  J
  Y / Y                                    Y   L
  | | |          \                         |   L
  | | |           Y                        A  J
  |   I           |                       /I\ /
  |    \          I             \        ( |]/|
  J     \         /._           /        -tI/ |
   L     )       /   /'-------'J           `'-:.
   J   .'      ,'  ,' ,     \   `'-.__          \ 
    \ T      ,'  ,'   )\    /|        ';'---7   /
     \|    ,'L  Y...-' / _.' /         \   /   /
      J   Y  |  J    .'-'   /         ,--.(   /
       L  |  J   L -'     .'         /  |    /\ 
       |  J.  L  J     .-;.-/       |    \ .' /
       J   L`-J   L____,.-'`        |  _.-'   |
        L  J   L  J                  ``  J    |
        J   L  |   L                     J    |
         L  J  L    \                    L    \ 
         |   L  ) _.'\                    ) _.'\ 
         L    \('`    \                  ('`    \ 
          ) _.'\`-....'                   `-....'
         ('`    \ 
          `-.___/   
""")
