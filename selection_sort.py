def selection_sort(arr):
    for i in range(len(arr)):
        cur_min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min]:
                cur_min = j
        temp = arr[i]
        arr[i] = arr[cur_min]
        arr[cur_min] = temp
