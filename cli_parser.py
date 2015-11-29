#!/usr/bin/env python3

# -*- coding: utf8 -*-

"""
This library provide the command line analyse, and verification.
"""

import argparse
import os


def parser_read_arg(args):
    """ Read cli argument and check if content the good value for parser"""

    parser = __parser_create_parser()

    arg = vars(parser.parse_args(args))

    if arg["unicorn"]:
        __unicorn()

    if not arg["stopword_fr"] and not arg["stopword_en"]:
        if __stopword():
            print("""
            We can't download nltk stop word or you didn't want.
            Please use option --stopword-french and --stopword-english
            """)
            return None

    return arg


def __parser_create_parser():
    """ Create the parser of argument for email parser """

    parser = argparse.ArgumentParser(prog="adt project email parser",
                                     formatter_class=argparse.
                                     ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--input", type=__isdir, required=True,
                        help="directory content one dir per month")
    parser.add_argument("-o", "--output", type=__output_check, required=True,
                        help="prefix of all output file")

    parser.add_argument("--stopword-fr", type=__isfile,
                        help="We use french stop word file.")
    parser.add_argument("--stopword-en", type=__isfile,
                        help="We use english stop word file.")

    parser.add_argument("-d", "--debug", action='store_true',
                        help="Activate debug mode")

    # easter egg
    parser.add_argument("--unicorn", action='store_true',
                        help=argparse.SUPPRESS)

    return parser


def analysis_read_args(args):
    """Read cli argument and check if content the good value for analise"""

    parser = __analysis_create_parser()

    arg = vars(parser.parse_args(args))

    if arg["unicorn"]:
        __unicorn()

    if arg["all_terms"] and arg["best_terms"] and arg["strict_terms"]:
        print("We can't use many terms option in same time")
        return None

    if arg["query"] and not (arg["all_terms"] or arg["best_terms"] or arg["strict_terms"]):
        print("Query need you use terms option")
        return None

    if arg["threshold"] == None and (arg["all_terms"] or arg["best_terms"] or arg["strict_terms"]) :
        print("We need threshold value when you use terms option")
        return None
        
    if (arg["all_terms"] and arg["best_terms"]) or (arg["all_terms"] and arg["strict_terms"]) or (arg["best_terms"] and arg["strict_terms"]) :
        print("We can't use some terms option sorry.")
        return None
    
    return arg


def __analysis_create_parser():
    """Create the parser of argument for analyse tools """
    
    parser = argparse.ArgumentParser(prog="adt project analyze",
                                     formatter_class=argparse.
                                     ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--input", type=str, required=True,
                        help="file content the result of parser")
    parser.add_argument("-q", "--query", nargs='+', type=str,
                        help="tag you query")
    parser.add_argument("-p", "--print-tag", action='store_true',
                        help="print all tag, default action")
    parser.add_argument("-a", "--all-terms", action='store_true',
                        help="print all terms in each tag")
    parser.add_argument("-b", "--best-terms", action='store_true',
                        help="print terms with good score")
    parser.add_argument("-s", "--strict-terms", action='store_true',
                        help="print just terms is in all tags")
    parser.add_argument("-t", "--threshold", type=float,
                        help="didn't print terms with lower threshold")

    # easter egg
    parser.add_argument("--unicorn", action='store_true',
                        help=argparse.SUPPRESS)

    return parser

def __stopword():
    """ Try if nltk stop word is download if not propose to download it """
    try:
        from nltk.corpus import stopwords
    except ImportError:
        answer = input("You want download nltk stopword [y/n] : ")
        while answer.lower() not in ['y', 'n']:
            answer = input("Please answer with [y/n] : ")

        if answer.lower() == "y":
            import nltk
            return nltk.download("stopwords")
        else:
            return False


def __isfile(val):
    """Check  if the path is leading to a file."""
    val = str(val)

    if not os.path.isfile(val):
        raise argparse.ArgumentTypeError(val+" is not a file")

    return val


def __isdir(val):
    """Check  if the path is leading to a directory."""
    val = str(val)

    if not os.path.isdir(val):
        raise argparse.ArgumentTypeError(val+" is not a directory")

    return val


def __output_check(val):
    """Check  if the path is leading to a directory."""
    val = str(val)
    total_path = ""
    for dir_name in os.path.splitext(os.path.dirname(val)):
        total_path = os.path.join(total_path, dir_name)
        if not os.path.isdir(total_path):
            raise argparse.ArgumentTypeError(total_path+"  is not a directory")

    return val


def __unicorn():
    """Friendship is magic!"""
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
