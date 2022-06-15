# TODO try implementing in place https://www.youtube.com/watch?v=Hoixgm4-P4M
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_idx = len(arr)//2
    below, above = [], []
    for i in range(len(arr)):
        if i == pivot_idx:
            continue

        if arr[i] <= arr[pivot_idx]:
            below.append(arr[i])
        else:
            above.append(arr[i])

    return quick_sort(below) + [arr[pivot_idx]] + quick_sort(above)

