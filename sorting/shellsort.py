#do this again its hard to understand

def shellsort(arr):
    sublistcount = len(arr)/2
    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)
        sublistcount = sublistcount / 2

def gap_insertion_sort(arr,start,gap):
    for i in range(start)


arr = []
shellsort(arr)
