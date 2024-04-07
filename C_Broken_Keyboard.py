# Function to solve the problem for a single test case
def solve_test_case(s):
    # Create a frequency dictionary to count occurrences of each letter
    freq_dict = {}
    for letter in s:
        freq_dict[letter] = freq_dict.get(letter, 0) + 1

    # Initialize the result string
    res = ""

    # Iterate through the frequency dictionary
    for letter, count in freq_dict.items():
        # If the count is odd, it must be produced by a working button
        if count % 2 == 1:
            res += letter

    # Sort the result string in alphabetical order
    res = ''.join(sorted(res))

    return res

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input string for the test case
    s = input().strip()

    # Solve the test case and print the result
    print(solve_test_case(s))
