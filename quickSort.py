def quick_sort(list):
    start = 0
    end = len(list)-1
    return quickSort(list, start, end)

def quickSort(list, start, end):

    if(start >= end):
        return list

    # pick the pivot
    middle = start + (end - start) / 2
    pivot = list[middle]

    # make left < pivot and right > pivot
    i = start
    j = end

    while i <= j:
        while list[i] < pivot:
            i = i + 1
        while list[j] > pivot:
            j = j -1
        if i <= j:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i = i + 1
            j = j - 1

    # recursively sort two sub parts
    if start < j:
        quickSort(list, start, j)

    if end > i:
        quickSort(list, i, end)
    return list


print(quick_sort([7,1,3,9,2]))