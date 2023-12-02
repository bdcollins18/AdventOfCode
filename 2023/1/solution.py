#!/usr/bin/python3

import sys
import os

containing_folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(containing_folder, 'input')

def parse_input():
    with open(input_path, 'w+') as input_file:
        return input_file.readlines

def part_1():
    input = parse_input()
    print('The solution to part 1 is ""!')

def part_2():
    input = parse_input()
    print('The solution to part 2 is ""!')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: solution [1|2]")
        exit(1)
    if sys.argv[1] not in ['1', '2']:
        print("usage: solution [1|2]")
        exit(1)
    if sys.argv[1] == '1':
        part_1()
    if sys.argv[1] == '2':
        part_2()
