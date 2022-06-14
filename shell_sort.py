def shell_sort(arr):
    # set up gap. 
    gap = len(arr)//2
    while gap > 0: 
        for right in range(gap, len(arr)): 
            temp = arr[right]
            # basically just insertion sort with gap size.
            while right-gap >= 0 and arr[right-gap] > temp: 
                arr[right] = arr[right-gap]
                right -= gap
            arr[right] = temp
        # modify the gap
        gap = gap//2


