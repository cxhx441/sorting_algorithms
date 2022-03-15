def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_idx = len(arr)//2
    arr_less, arr_greater = [], []
    for i in range(len(arr)):
        if i == pivot_idx:
            continue

        if arr[i] <= arr[pivot_idx]:
            arr_less.append(arr[i])
        else:
            arr_greater.append(arr[i])

    return quick_sort(arr_less) + [arr[pivot_idx]] + quick_sort(arr_greater)
