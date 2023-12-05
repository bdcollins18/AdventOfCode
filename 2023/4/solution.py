#!/usr/bin/python3

import sys
import os
import collections
import re

containing_folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(containing_folder, 'input')

Card = collections.namedtuple('Card', 'card_num winning_nums your_nums')

def parse_input():
    pat = re.compile(r'Card\s+(\d+):\s+((\d+\s+)+)\|\s+((\d+\s+)+)')
    sep_pat = re.compile(r'\s+')
    
    with open(input_path, 'r') as input_file:
        for line in input_file:
            match = pat.match(line)
            card_num = int(match.group(1))
            winning_nums = [int(m) for m in sep_pat.split(match.group(2))[:-1]]
            your_nums = [int(m) for m in sep_pat.split(match.group(4))[:-1]]
            yield Card(card_num, winning_nums, your_nums)
            

def part_1():
    input = parse_input()
    total = 0
    for card in input:
        wins = [n for n in card.your_nums if n in card.winning_nums]
        num_wins = len(wins)
        if num_wins > 0:
            total += pow(2, num_wins - 1)
    print(total)
        
def part_2():
    input = parse_input()
    card_multiples = dict()
    for card in input:
        
        card_multiple = card_multiples.get(card.card_num, 0) + 1
        card_multiples[card.card_num] = card_multiple
        num_wins = len([n for n in card.your_nums if n in card.winning_nums])
        for i in range(card.card_num + 1, card.card_num + 1 + num_wins):
            card_multiples[i] = card_multiples.get(i, 0) + card_multiple
    print(sum(card_multiples.values()))

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
