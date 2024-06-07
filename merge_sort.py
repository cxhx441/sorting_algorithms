def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[0:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    while l < len(left):
        merged.append(left[l])
        l += 1
    while r < len(right):
        merged.append(right[r])
        r += 1
    return merged

