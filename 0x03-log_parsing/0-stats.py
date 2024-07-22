#!/usr/bin/python3
"""This script reads stdin line by line"""
from sys import stdin

cache = {
    '200': 0,
    '301': 0,
    '400': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
    }
tot_size = 0
counter = 0

def prn_stats():
    """
    Function that print stats about log
    """

    print(f'File size: {tot_size}')
    stcdor = sorted(cache.keys())
    for each in stcdor:
        if cache[each] > 0:
            print(f'{each}: {cache[each]}')


if __name__ == "__main__":
    try:
        for data in stdin:
            try:
                fact = data.split(' ')
                if fact[-2] in cache:
                    cache[fact[-2]] += 1
                tot_size += int(fact[-1])
            except:
                pass
            counter += 1
            if counter == 10:
                prn_stats()
                counter = 0
    except KeyboardInterrupt:
        prn_stats()
        raise
    else:
        prn_stats()