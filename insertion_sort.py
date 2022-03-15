def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur_item:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur_item
