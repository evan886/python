def  solve():
    n = int(input())
    arr = list(map(int,input().split()))

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in  range(2,n +1):
        for i in range(n - length + 1):
            j = i + length -1
            if arr[i] == arr [j]:
                dp[i][j] = dp[i+1][j-1] +2
            else:
                if dp[i+1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i][j-1]

    def reconstruct(i,j):
        if i > j:
            return []
        if arr[i] == arr[j]:
            return [arr[i]] + reconstruct(i+1,j-1) + [arr[j]]
        else:
            if dp[i+1][j] > dp[i][j-1]:
                return  reconstruct(i+1,j)
            else:
                return reconstruct(i,j-1)

    result = reconstruct(0,n-1)
    print(' '.join(map(str,result)))

solve()