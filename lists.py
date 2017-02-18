def sum_list(str):
    i = 0
    sum = 0
    for each in str:
        sum = sum + each
    return sum

print sum_list([1,2,3])

#largest number in the list
def large(str):
    for each in str:

        return max(str)

print large([1,3,8,6,89,9])

#list sorted in increasing order by the last element in each tuple
def last(n):
    return n[-1]

def list_tuple(str):
   for each in str:
        return sorted(str, key=last)



print list_tuple([(2,5),(1,2),(4,4),(2,3),(2,1)])

#Lets check if it works.