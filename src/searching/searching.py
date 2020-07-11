def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = (len(arr) - 1)
    while high >= low and not False:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        else:
            if guess > target:
                high = middle - 1
            if guess < target:
                low = middle + 1
    return -1  # not found
