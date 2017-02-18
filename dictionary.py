import operator

def sortDict(list):
    #return sorted(list.items(), key=operator.itemgetter(0))
    return sorted(list.items(), key=operator.itemgetter(0), reverse=True)


print(sortDict({1:10, 2:20, 7:70, 3:30}))

def ConctDict(dict, dict1):
    list = dict.items()+dict1.items()
    return list

print(ConctDict({1:10, 2:20}, {3:30}))

def keyExists(dict, n):

    if n in dict:
        print('yes')
    else:
        print('no')
keyExists({1:0, 2:3}, 3)