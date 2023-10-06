MOD = 998244353

def ValidCombinations(A, B, C):
    dp = [[0 for _ in range(C + 1)] for _ in range(A + 1)]

    # Base case: there is only one way to select zero integers
    dp[0][0] = 1

    for i in range(1, A + 1):
        for j in range(1, C + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j] * (B - j + 1)) % MOD
            dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (B - 1)) % MOD

    return dp[A][C]

def main():
    A = int(input())
    B = int(input())
    C = int(input())

    result = ValidCombinations(A, B, C)
    print(result)

if __name__ == "__main__":
    main()