#!/usr/bin/python3

import sys
import os
import functools

containing_folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(containing_folder, 'input')

def parse_input(): 
    with open(input_path, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            game_str, rounds_str = line.split(': ')
            game_num = int(game_str.split(' ')[1])
            round_strs = (round for round in rounds_str.split('; '))
            handful_strs_by_round = (round_str.split(', ') for round_str in round_strs)
            rounds = (((lambda h: (int(h[0]),h[1]))(handful_str.split(' ')) for handful_str in handful_strs) for handful_strs in handful_strs_by_round)
            yield (game_num, rounds)
                

def part_1():
    games = parse_input()
    maxes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible_game_nums = []
    for game_num, rounds in games:
        is_possible = True
        for round in rounds:
            for handful in round:
                if handful[0] > maxes[handful[1]]:
                    is_possible = False
                    break
            if not is_possible:
                break
        if is_possible:
            possible_game_nums.append(game_num)
    print(sum(possible_game_nums))

def part_2():
    games = parse_input()
    bag_powers = []
    for game_num, rounds in games:
        mins = {
            'red':0,
            'green':0,
            'blue':0
        }
        for round in rounds:
            for handful in round:
                if handful[0] > mins[handful[1]]:
                    mins[handful[1]] = handful[0]
        bag_powers.append(functools.reduce(lambda x,y: x*y, mins.values()))
    print(sum(bag_powers))

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
