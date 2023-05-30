def selection_sort(nums):
    size = len(nums)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if nums[j] < nums[min_index]:
                i = j
        (nums[i], nums[min_index]) = (nums[min_index], nums[i])


numbers = [7, 3, 8, 1, 4, 5, 2, 6]
selection_sort(numbers)
print(numbers)