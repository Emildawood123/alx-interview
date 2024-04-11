#!/usr/bin/python3
"""GfG class"""
class GfG:
    """GfG class"""
    def __init__(self):
        """init method"""
        self.MAX = 10
        self.arr = [0] * self.MAX

    def canPlace(self, k, i):
        """canPlace method"""
        for j in range(1, k):
            if (self.arr[j] == i or
               (abs(self.arr[j] - i) == abs(j - k))):
                return False
        return True
 
    def display(self, n):
        """display method"""
        arr = []
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if self.arr[i] != j:
                    continue
                else:
                    arr.append([i - 1, j - 1])
        print(arr)
 
    def nQueens(self, k, n):
        """nQueens"""
        for i in range(1, n + 1):
            if self.canPlace(k, i):
                self.arr[k] = i
                if k == n:
                    self.display(n)
                else:
                    self.nQueens(k + 1, n)
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("Usage: nqueens N")
        exit(1)
    convert = int(sys.argv[1])
    if type(convert) != int:
        print("N must be a number")
        exit(1)
    if convert < 4:
        print("N must be at least 4")
        exit(1)
    n = convert
    obj = GfG()
    obj.nQueens(1, n)
