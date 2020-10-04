def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentValue = arr[i]
        position = i

        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position = position-1
        arr[position] = currentValue
    print(arr)


arr = [5, 3, 2, 1, 4]
insertion_sort(arr)
