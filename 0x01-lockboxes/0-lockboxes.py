#!/usr/bin/python3
""" open all boxes """


def canUnlockAll(boxes):
    """canUnlockAll"""
    boxes_status = [0] * len(boxes)
    boxes_status[0] = 1
    is_have_all_keys = recursion_function(boxes, boxes[0], boxes_status)
    return is_have_all_keys


def recursion_function(boxes, unlockBox, boxes_status):
    """recursion_function"""
    if len(unlockBox) == 0 and 0 in boxes_status:
        return False
    elif len(unlockBox) == 0 and 0 not in boxes_status:
        return True
    new = []
    for key in unlockBox:
        if key > len(boxes) - 1:
            continue
        if boxes_status[key] == 0:
            new = new + boxes[key]
            boxes_status[key] = 1
    return recursion_function(boxes, new, boxes_status)
