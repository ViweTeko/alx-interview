#!/usr/bin/env python3
""" UTF-8 Validation"""


def validUTF8(data):
    """Determines if UTF-8 encoding is valid"""
    bytes_num = 0
    m1 = 1 << 7
    m2 = 1 << 6
    for byte in data:
        byte_mask 1 << 7
        if bytes_num == 0:
            while byte & byte_mask:
                bytes_num += 1
                byte_mask = byte_mask >> 1
            if bytes_num == 0:
                continue
            if bytes_num == 1 or bytes_num > 4:
                return False
        else:
            if not (byte & m1 and not (byte & m2)):
                return False
        bytes_num -= 1
    if bytes_num == 0:
        return True
    return False
