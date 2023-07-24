def TwoNumberSum(array, targetSum):
    for i in range(0, len(array)):
        for j in reversed(range(len(array))):
            print(array[i], array[j])
            if array[i] + array[j] == targetSum:
                return array[i], array[j]
            elif j <= len(array)/2:
                print("Break")
                break
    return []


parent_array = [3, 5, -4, 8, 11, 1, -1, 6]
parent_targetSum = 13
# TwoNumberSum(parent_array, parent_targetSum)
print(TwoNumberSum(parent_array, parent_targetSum))
