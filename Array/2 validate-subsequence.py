def isValidSubsequence(array, sequence):
    # Write your code here.
    array_stage = 0
    found = 1
    for i in range(0, len(sequence)):
        if found == 1:
            found = 0
        else:
            return False
        for j in range(array_stage, len(array)):
            print(sequence[i], array[j])
            if sequence[i] == array[j]:
                found = 1
                array_stage = j + 1
                break
            
    if found == 1:
        return True
    else:
        return False


parent_array = [5, 1, 22, 25, 6, -1, 8, 10]
parent_sequence = [5, 1, 22, 25, 6, -1, 8, 10, 22]
print(isValidSubsequence(parent_array, parent_sequence))
