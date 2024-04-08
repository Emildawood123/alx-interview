#!/usr/bin/python3
"""Queens interview"""
import sys
def initailize_with_first(first_row, n):
    table = []
    table.append(first_row)
    for row in range(1, n):
        tables_second = list(map(lambda x: x[1], table))
        for stage in range(n):
            try:
                if stage == 0:
                    if stage in tables_second:
                        continue
                    elif table[row - 1][1] != stage + 1:
                        table.append([row, stage])
                        break
                    else:
                        continue
                elif stage == n - 1:
                    if stage in tables_second:
                        continue
                    elif table[row - 1][1] != stage - 1:
                        table.append([row, stage])
                        break
                    else:
                        continue
                else:
                    if stage in tables_second:
                        continue
                    elif table[row - 1][1] != stage + 1 and table[row - 1][1] != stage - 1:
                        table.append([row, stage])
                        break
                    else:
                        continue
            except Exception:
                return False
    if len(table):
        return table

if len(sys.argv) == 1:
    print("Usage: nqueens N")
    exit(1)
else:
    after_convert = int(sys.argv[1])
    if type(after_convert) != int:
        print("N must be a number")
        exit(1)
    elif after_convert < 4:
        print("N must be at least 4")
        exit(1)
    else:
        tables = []
        for i in range(after_convert):
            first_row = [0, i]
            table = initailize_with_first(first_row, after_convert)
            if type(table) == list:
                tables.append(table)
            else:
                continue
        for i in tables:
            print (i)