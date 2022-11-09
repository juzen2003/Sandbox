#!/usr/bin/env python3

import argparse
import functools
import logging
import sys
from datetime import datetime

parser = argparse.ArgumentParser(prog = 'simple_math.py',
                                 description = 'Do some simple math.')

parser.add_argument('nums', nargs='*', type=int, 
                    help='Variables we want to pass into the program.') 

parser.add_argument('--add', '-a', action='store_true',
                    help='Perform continuous "+" operations on passed in nums')

parser.add_argument('--minus', '-m', action='store_true',
                    help='Perform continuous "-" operations on passed in nums in order')

parser.add_argument('--times', '-t', action='store_true',
                    help='Perform continuous "*" operations on passed in nums in order')

parser.add_argument('--divide', '-d', action='store_true',
                    help='Perform continuous "/" operations on passed in nums in order')

args = parser.parse_args()

def calculate(nums):
    res = 0
    if args.add:
        res = sum(args.nums)
    elif args.minus:
        res = functools.reduce(lambda a, b: a-b, args.nums)
    elif args.times:
        res = functools.reduce(lambda a, b: a*b, args.nums)
    elif args.divide:
        try:
            res = functools.reduce(lambda a, b: a/b, args.nums)
        except ZeroDivisionError:
            logging.error("ZeroDivisionError")
            logging.warning("ZeroDivisionError but will return 0 as the result")
            res = 0
    print(res)
    return res

def main():
    # current_time = datetime.now().strftime("%H:%M:%S")
    # logging.basicConfig(filename=f'simple_math_{current_time}.log', 
    #                     encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(filename=f'simple_math.log', 
                        encoding='utf-8', level=logging.DEBUG)
    logging.info("List out all argument.")
    print(sys.argv)
    logging.info("Run the main task.")
    calculate(args.nums)

main()


