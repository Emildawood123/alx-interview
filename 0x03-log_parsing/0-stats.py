#!/usr/bin/python3
import fileinput
import requests
for fileinput_line in fileinput.input():
    if ('stop' == fileinput_line.rstrip()):
        break
    print(fileinput_line)
