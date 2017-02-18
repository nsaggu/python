def change_string(str):
    str_not = str.find('not')
    str_poor = str.find('poor')
    if str_poor > str_not:
        str = str.replace(str[str_not:(str_poor+4)], 'good')
    return str
print(change_string("The lyrics is not that poor"))


def str_length(str1):
    word_len = []
    for n in str1:
        word_len.append(len(n))
        max_length = max(word_len)
    for n in str1:
        if len(n) == max_length:
            return n

print(str_length(["My" ,"Harinder", "name", "Navneet"]))

def unique_str():

    temp = []
    list = raw_input("Enter list")
    sort = sorted(set(list))
    return sort
print(unique_str())

#remove characters which hav odd index values of a given string
def odd_index(str2):

    list = str2[1::2]
    return list
print odd_index("love")
