# binary search o(logN)
def binary_search(array,item,left,right):

    # base case for recursive function call
    # this is the search miss (array does not contain the item)
    if right < left:
        return -1
    # generate the middle item's index
    middle = left + (right-left)//2
    print("Middle index: ",middle)

    # the middle item we r looking for
    if array[middle] == item:
        return middle

    # the item is the smaller than the middle item
    # so we consider the left subarray
    elif array[middle] > item:
        print("Checking items on the left...")
        return binary_search(array,item,left,middle-1)

    # the item is greater than middle one
    # then we have to consider right subarray
    elif array[middle] < item:
        print("Checking items on the right...")
        return binary_search(array,item,middle+1,right)


if __name__ == "__main__":

    array = [1,5,6,7,9,11,25,35,48,59]
    print(binary_search(array,25,0,len(array)-1))