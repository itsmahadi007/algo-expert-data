"""
Task 1:
Write a function that does the following task.

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.


Constraints:
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""


def searching(arr, target):
    l, r = 0, len(arr) - 1
    n = len(arr)
    while l <= r:
        mid = (l + r) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

numbers = [-1, 0, 3, 5, 9, 12]
target = 9
result = searching(numbers, target)
print(result)



"""
Task 2:
Write a function that does the following task.
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
    
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

"""


def rotation_search(arr):
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid - 1
            
    return arr[low]


numbers = [4,5,6,7,0,1,2]
result = rotation_search(numbers)
print(result)
