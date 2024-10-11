def solve():
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Length of the array
        a = list(map(int, input().split()))  # The array

        if n == 1:
            # If there's only one element, the score is that element + 1 (since count is 1)
            print(a[0] + 1)
            continue

        # Initialize dp array where dp[i] represents the maximum score up to the i-th element
        dp = [0] * n

        # Base cases:
        dp[0] = a[0] + 1  # Color the first element
        dp[1] = max(a[0], a[1]) + 1  # Either color first or second element, can't color both

        # Fill dp array using the transition rule:
        for i in range(2, n):
            # Either take the previous score without coloring current, or take the score two steps back and color current
            dp[i] = max(dp[i-1], dp[i-2] + a[i] + 1)

        # The result for this test case is the maximum score at dp[n-1]
        print(dp[n-1])

# Running the function
if __name__ == "__main__":
    solve()
