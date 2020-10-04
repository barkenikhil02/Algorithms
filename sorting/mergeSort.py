def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)/2
        lefthalf = arr[:int(mid)]
        righthalf = arr[int(mid):]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
    print(arr)

arr = [5, 3, 2, 1, 4]
MergeSort(arr)
print(arr)