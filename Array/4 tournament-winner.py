def tournamentWinner(competitions, results):
    # Write your code here.
    # print(competitions, results)
    dic = {}
    for i in range(0, len(competitions)):
        if results[i] == 0:
            dic = dict_update(dic,competitions[i][1])
        elif results[i] ==1:
            dic = dict_update(dic, competitions[i][0])
        print(dic)        
        
    max_key = max(dic, key=dic.get)
    return max_key

def dict_update(dic,win):
    # print(dic.get(win))
    # if dic.get(win) is not None:
    if win in dic:
        dic[win] = dic.get(win) + 3
    else:
        dic[win] = 3
    return dic

competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]
expected = "Python"
actual = tournamentWinner(competitions, results)
print(actual)