def max_subarray_sum(arr):
    max_so_far = 0
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum = max((arr[i] + cur_sum), arr[i])
        max_so_far = max(max_so_far, cur_sum)
    return max_so_far


arr = [2, -3, 4, -5]
print(max_subarray_sum(arr))
