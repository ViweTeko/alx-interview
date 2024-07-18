#!/usr/bin/env python3
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

try:
    for line in stdin:
        line_ls = line.split(" ")
        if len(line_ls) > 4:
            code = line_ls[-2]
            size = int(line_ls[-1])
            if code in cache.keys():
                cache[code] += 1
                tot_size += size
                counter += 1

            if counter == 10:
                counter = 0
                print(f'File size: {tot_size}')
                
                for key, value in sorted(cache.items()):
                    if value != 0:
                        print(f'{key}: {value}')
except Exception as error:
    pass
finally:
    print(f'File size: {tot_size}')
    for key, val in sorted(cache.items()):
        if val != 0:
            print(f'{key}: {val}')