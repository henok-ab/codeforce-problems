def is_possible(nums, k):
    n = len(nums)
    for i in range(n):
        total = sum(nums) - nums[i]  # Sum of all elements except nums[i]
        if (n - 1) * nums[i] == total and nums[i] == k:
            return True
    return False

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read n and k for the current test case
    n, k = map(int, input().split())
    # Read the list of integers
    nums = list(map(int, input().split()))
    
    # Check if it's possible to achieve k with n-1 operations
    if is_possible(nums, k):
        print("YES")
    else:
        print("NO")
