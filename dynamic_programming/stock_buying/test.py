from dynamic_programming.stock_buying.method import max_profit_single_transaction_dp
from dynamic_programming.stock_buying.method import max_profit_with_cooldown_dp
from dynamic_programming.stock_buying.method import max_profit_with_cooldown_dfs
from dynamic_programming.stock_buying.method import max_profit_single_transaction_dp_states

print('############################')
print('Testing Stock Buying with Cooldown')
print('############################')

prices = [1,2,3,0,2]
profit = max_profit_with_cooldown_dfs(prices)
assert profit == 3, "Expected profit: {}; received {}".format(3, profit)

prices = [1,2,3,0,2]
profit = max_profit_with_cooldown_dp(prices)
assert profit == 3, "Expected profit: {}; received {}".format(3, profit)

print('############################')
print('Testing Stock Buying: singly buy and sell')
print('############################')

def max_profit_single_transaction_bf(prices):
    profit, numPrices = 0, len(prices)

    for i, price in enumerate(prices):
        for j in range(i + 1, numPrices):
            profit = max(profit, prices[j] - price)

    return profit

prices_collection = [[1,2,3,0,1], [1,2,1,10,5], [10,2,3,0,2], [10,9,3,2,1]]

for prices in prices_collection:
    brute, dp = max_profit_single_transaction_bf(prices), max_profit_single_transaction_dp(prices)
    assert brute == dp, "Expected {}; Received: {}".format(brute, dp)

for prices in prices_collection:
    brute, dp = max_profit_single_transaction_bf(prices), max_profit_single_transaction_dp_states(prices)
    assert brute == dp, "Expected {}; Received: {}".format(brute, dp)
