# TODO try implementing in place https://www.youtube.com/watch?v=Hoixgm4-P4M
def quick_sort_in_place(arr):
    def helper(left, right):
        if left >= right:
            return
        i = left
        j = right
        pivot = ((j-i) // 2) + i
        # swap element at pivot and end
        arr[pivot], arr[j] = arr[j], arr[pivot]
        pivot = j
        j -= 1
        while i < j:
            if arr[i] <= arr[pivot]:
                i += 1
            elif arr[j] > arr[pivot]:
                j -= 1
            else:
                # swap element at left and right
                arr[i], arr[j] = arr[j], arr[i]

        # left and right are on same index
        # if arr[pivot] < arr[left], swap
        if arr[pivot] < arr[i]:
            arr[pivot], arr[i] = arr[i], arr[pivot]
            pivot = i
            helper(left, pivot-1)
            helper(pivot+1, right)
        else:
            helper(left, pivot-1)

    helper(0, len(arr)-1)
    return arr

# arr = [7, 3, 1, 4, 2, 6, 5]
# arr = [5, 4, 3, 2, 1]
# arr = [0, 0, 0, 0, 0]
# arr = [1, 2, 3, 4, 5]
# arr = [-1, -2, -3, -4, -5]
# arr = [100, -2, 40, -800, 1]
# arr = [10, 100, 5, 200, 1]
# print(arr)
# quick_sort_in_place(arr)
# print(arr)

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

