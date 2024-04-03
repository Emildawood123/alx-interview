#!/usr/bin/python3
"""validate_utf8 module"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""

    def byte_seq_c(byte):
        """return number"""
        leading_ones = 0
        while (byte >> 7 - leading_ones) & 1:
            leading_ones += 1
        return leading_ones
    i = 0
    while i < len(data):
        seq_c = byte_seq_c(data[i])
        if seq_c == 0:
            i += 1
            continue
        if seq_c == 1 or seq_c > 4 or i + seq_c > len(data):
            return False
        for j in range(1, seq_c):
            if not (data[i + j] >> 6 == 0b10):
                return False

        i += seq_c

    return True
