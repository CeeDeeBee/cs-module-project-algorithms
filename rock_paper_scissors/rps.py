#!/usr/bin/python

import sys


def recurse(n, options, output, sub_arr=[]):
    if n == 0:
        output.append(sub_arr)
        return
    for option in options:
        new_arr = sub_arr[:]
        new_arr.append(option)
        recurse(n - 1, options, output, new_arr)


def rock_paper_scissors(n):
    # Your code here
    options = ["rock", "paper", "scissors"]
    output = []
    recurse(n, options, output)
    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
