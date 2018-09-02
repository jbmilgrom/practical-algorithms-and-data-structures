from dynamic_programming.stock_buying.method import max_profit_dfs

print('############################')
print('Testing Stock Buying')
print('############################')

prices = [1,2,3,0,2]

profit = max_profit_dfs(prices)
assert profit == 3, "Expected profit: {}; received {}".format(3, profit)

