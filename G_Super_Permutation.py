def super_permutation(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]

    # Check if a super-permutation is possible
    if n <= 3:
        return -1

    # Initialize the super-permutation array
    super_perm = [0] * n

    # Start constructing the super-permutation
    for i in range(n - 1):
        super_perm[i] = i + 1

    # Calculate the last element of the super-permutation
    last_element = 0
    for i in range(n - 1):
        last_element += super_perm[i]
        last_element %= n

    # Check if the last element is distinct from others
    if last_element in super_perm[:n - 1]:
        return -1

    super_perm[-1] = last_element + 1

    return super_perm

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the length of the desired permutation
    n = int(input())

    # Get the super-permutation for the current test case
    result = super_permutation(n)

    # Output the result
    if result == -1:
        print(-1)
    else:
        print(" ".join(map(str, result)))

