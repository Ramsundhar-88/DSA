def secondLargestElement(nums):
    largest = float('-inf')
    second_largest = float('-inf')

    for x in nums:
        if x > largest:
            second_largest = largest
            largest = x
        elif second_largest < x < largest:
            second_largest = x

    if second_largest == float('-inf'):
        return -1
    return second_largest

print(secondLargestElement([3,5,5,8,9]))