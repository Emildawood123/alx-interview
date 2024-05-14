pseudo code:-
-------------
ben_score = 0
maria_score = 0
loop in the main_list
    create range(1, item + 1)
    ben_score_round = 0
    maria_score_round = 0
    whose_play = 2
    index = 0
    while new_list != [] && new_list has prime numbers
        for i in new_list:
            if i is primsenumber:
                for s in new_list:
                    if s % i == 0:
                        new_list.remove(s)
        if whose % 2 == 0:
            maria_score_round += 1
        else:
            ben_score_round += 1
        whose_play += 2
    if len(new_list) > 0:
        if whose_play % 2 == 0
            ben_score += 1
        else:
            maria_score += 1
    else:
        if maria_score_round > ben_score_round:
            maria_score += 1
        else:
            ben_score += 1
if maria_score > ben_score
    print("maria winner")
else
    print("ben winner")
    
                

        
