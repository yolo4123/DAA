#Longest common sequence
def lcs(x,y):
    m=len(x)
    n=len(y)
    dp=[ [0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range( i ,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1] + 1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

x=input("s1:")
y=input('s2:')
print("length of lcs is:",lcs(x,y))