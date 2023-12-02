#!/usr/bin/python3

import sys
import os

import re

containing_folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(containing_folder, 'input')

def parse_input():
    with open(input_path, 'r') as input_file:
        return input_file.readlines()

def part_1():
    input = parse_input()
    pat = re.compile(r'\d')
    total = 0
    for line in input:
        matches = pat.findall(line)
        total += int(matches[0] + matches[-1])
    print(total)

def part_2():
    input = parse_input()
    tokens = {
        '0':'0',
        'zero':'0',
        '1':'1',
        'one':'1',
        '2':'2',
        'two':'2',
        '3':'3',
        'three':'3',
        '4':'4',
        'four':'4',
        '5':'5',
        'five':'5',
        '6':'6',
        'six':'6',
        '7':'7',
        'seven':'7',
        '8':'8',
        'eight':'8',
        '9':'9',
        'nine':'9',
    }
    pat = re.compile(f'(?=({"|".join(tokens.keys())}))')
    total = 0
    for line in input:
        matches = pat.findall(line)
        total += int(tokens[matches[0]]+tokens[matches[-1]])
    print(total)

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
