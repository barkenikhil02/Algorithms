def linear_search(array,item):
    # simple linear search in o(n) running time complexity
    for i in range(len(array)):
        # we have founf the given item so return with the index
        if array[i] == item:
            return  i
    
    # search missed: item not found
    return -1

if __name__ == "__main__":
    array = [24,3,25,5,3,22,7575,3,4,6]
    print(linear_search(array,22))