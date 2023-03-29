'''
i = 1, j = 0, k = 0
tmp_sum = dp[0][0] + dp[1][1] + products[0][0] * matrices[1][1]
tmp_sum = 0 + 0 + 15 * 2
dp[0][1] = 3
i = 1, j = 1, k = 0
tmp_sum = dp[1][1] + dp[2][2] + products[1][1] * matrices[2][1]
tmp_sum = 0 + 0 + 6 * 6
dp[1][2] = 36

i = 2, j = 0, k = 0
tmp_sum = dp[0][0] + dp[1][2] + \
    products[0][0] * matrices[2][1]
tmp_sum = 0 + 36 + 15*6
    
dp[0][2] = 126


i = 2, j = 0, k = 1
tmp_sum = dp[0][1] + dp[2][2] + \
    products[0][1] * matrices[2][1]

tmp_sum = 30 + 0 + 10 * 6
dp[0][2] = 90
'''

