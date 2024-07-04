#!/usr/bin/python3
""" This script determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """This function takes list of lists and content of list unlocks lists"""
    # This variable creates set of box(es) being checked
    checked = set()
    checked.add(0)
    stack = [0]

    while stack:
        curr = stack.pop()
        for key in boxes[curr]:
            if key < len(boxes) and key not in checked:
                checked.add(key)
                stack.append(key)
    return len(checked) == len(boxes)
