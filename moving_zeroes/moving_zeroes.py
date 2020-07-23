'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # new_arr = [0] * len(arr)

    # loc = 0
    # for i in arr:
    #     if i is not 0:
    #         new_arr[loc] = i
    #         loc += 1

    # return new_arr

    # optimized
    left = 0
    right = len(arr) - 1

    while left < right:
        if not arr[left] and arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            if arr[left]:
                left += 1
            if not arr[right]:
                right -= 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
