#!/usr/bin/python3

import sys
import os

import re
import enum
import collections
import itertools

class TokenType(enum.Enum):
    NUMBER = 0
    SYMBOL = 1

Token = collections.namedtuple('Token', 'type line str span')

Line = collections.namedtuple('Line', 'numbers symbols')

containing_folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(containing_folder, 'input')

def parse_input():
    number_pat = re.compile('\d+')
    symbol_pat = re.compile('[^\d.]')
    with open(input_path, 'r') as input_file:
        for i, line in enumerate(input_file):
            line = line.strip()
            number_matches = number_pat.finditer(line)
            symbol_matches = symbol_pat.finditer(line)
            
            numbers = [Token(TokenType.NUMBER, i, match.group(0), match.span(0)) for match in number_matches]
            symbols = [Token(TokenType.SYMBOL, i, match.group(0), match.span(0)) for match in symbol_matches]
            yield Line(numbers, symbols)
 
def are_overlapping_adjacent(span_a, span_b):
    return (span_a[0] <= span_b[1]) and (span_b[0] <= span_a[1])
    
def pairwise(it):
    a, b = itertools.tee(it)
    next(b, None)
    return zip(a, b)

def part_1():
    input = parse_input()
    part_numbers = set()
    for cur, next in pairwise(input):
        for number in cur.numbers:
            for symbol in cur.symbols:
                if are_overlapping_adjacent(number.span, symbol.span):
                    part_numbers.add(number)
        
        for number in cur.numbers:
            for symbol in next.symbols:
                if are_overlapping_adjacent(number.span, symbol.span):
                    part_numbers.add(number)
        
        for number in next.numbers:
            for symbol in cur.symbols:
                if are_overlapping_adjacent(number.span, symbol.span):
                    part_numbers.add(number)

    print(sum(int(token.str) for token in part_numbers))

def multimap_add(dic, key, val):
    if key not in dic:
        dic[key] = [val]
    else:
        dic[key].append(val)
    

def part_2():
    input = parse_input()
    adjacent_to_gear = dict()
    
    for cur, next in pairwise(input):
        for number in cur.numbers:
            for symbol in cur.symbols:
                if symbol.str != '*':
                    continue
                if are_overlapping_adjacent(number.span, symbol.span):
                    multimap_add(adjacent_to_gear, symbol, number)
        
        for number in cur.numbers:
            for symbol in next.symbols:
                if symbol.str != '*':
                    continue
                if are_overlapping_adjacent(number.span, symbol.span):
                    multimap_add(adjacent_to_gear, symbol, number)
        
        for number in next.numbers:
            for symbol in cur.symbols:
                if symbol.str != '*':
                    continue
                if are_overlapping_adjacent(number.span, symbol.span):
                    multimap_add(adjacent_to_gear, symbol, number)
    
    print(sum(
        (int(nums[0].str) * int(nums[1].str)) for nums in adjacent_to_gear.values() if len(nums) == 2
        ))
            
    
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
