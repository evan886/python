def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # dp[i][j] = 从i到j的最长回文子序列长度
    dp = [[0] * n for _ in range(n)]
    # path[i][j] 用于记录选择，便于重构答案
    # 0: 两边都选（arr[i]==arr[j]）
    # 1: 跳过左边
    # 2: 跳过右边

    # 初始化：单个字符是长度为1的回文
    for i in range(n):
        dp[i][i] = 1

    # 按长度从小到大填表
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                if dp[i + 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    # 重构最长回文子序列
    def reconstruct(i, j):
        if i > j:
            return []
        if i == j:
            return [arr[i]]
        if arr[i] == arr[j]:
            # 两边都选
            return [arr[i]] + reconstruct(i + 1, j - 1) + [arr[j]]
        else:
            if dp[i + 1][j] > dp[i][j - 1]:
                return reconstruct(i + 1, j)
            else:
                return reconstruct(i, j - 1)

    result = reconstruct(0, n - 1)
    print(' '.join(map(str, result)))


solve()