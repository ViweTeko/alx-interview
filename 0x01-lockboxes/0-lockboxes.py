#!/usr/bin/python3
""" This script determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """This function takes list of lists and content of list unlocks lists"""
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and < len(boxes):
                keys.append(boxKey)

    if len(keys) == len(boxes):
        return True
    return False
