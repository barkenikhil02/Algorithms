def bubblesort(arr):
    for i in range(len(arr)-1, 0, -1):
        print(i)
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


arr = [5, 3, 2, 1, 4]
bubblesort(arr)
