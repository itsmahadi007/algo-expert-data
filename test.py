from math import sqrt


def count_full_square_pairs(numbers):
    n = len(numbers)
    # Create a set to store the square values
    squares = set(i * i for i in range(int(sqrt(2 * 10**5)) + 1))
    # Initialize a counter for the number of full square pairs
    count = 0
    # Use a dictionary to store the frequency of each number in the array
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    # Iterate through the frequency dictionary
    for num, freq in frequency.items():
        # Check if the sum of the current number and other numbers is a full square
        for square in squares:
            if square - num in frequency and square - num != num:
                count += freq * frequency[square - num]
        # Check if the sum of the current number and itself is a full square
        if num >= 0 and 2 * num in squares:
            count += freq * (freq - 1) // 2
    return count


numbers = [-1, 18, 3, 1, 5]
result = count_full_square_pairs(numbers)
print(result)
