#!/usr/bin/env python3
""" UTF-8 Validation"""


def validUTF8(data) -> bool:
    """Determines if UTF-8 encoding is valid"""
    bytes_num = 0
    for byte in data:
        mask = 1 << 7
        if not bytes_num:
            while byte & mask:
                bytes_num += 1
                mask >>= 1
            if not bytes_num:
                continue
            if bytes_num == 1 or bytes_num > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        bytes_num -= 1
    return bytes_num == 0
