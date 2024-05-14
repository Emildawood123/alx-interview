#!/usr/bin/python3
def isWinner(x, nums):
    def is_prime_arr(arr):
        for number in arr:
            if number <= 1:
                continue
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    continue
            return number
        return False
    ben_score = 0
    maria_score = 0
    for i in range(x):
        new_list = list(range(1, nums[i] + 1))
        ben_score_round = 0
        maria_score_round = 0
        whose_play = 2
        while new_list != [] and is_prime_arr(new_list) is not False:
            number = is_prime_arr(new_list)
            for i in new_list:
                if i % number == 0:
                    new_list.remove(i)
            whose_play += 1
            if whose_play % 2:
                maria_score_round += 1
            else:
                ben_score_round += 1
        if len(new_list) > 0 and whose_play % 2 == 0:
            ben_score += 1
        elif len(new_list) > 0 and whose_play % 2 != 0:
            maria_score += 1
        elif ben_score_round > maria_score_round:
            ben_score += 1
        else:
            maria_score += 1
    if maria_score == ben_score:
        return None
    return "Maria" if maria_score > ben_score else "Ben"
