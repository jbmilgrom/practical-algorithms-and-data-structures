# Understanding:
#   Each i in array represents a price at subquent day i
#   You can buy and sell n >= 0 times
#   You can't hold more than one stock at any given time
#   You can only buy stock more than one day after selling i.e. "cooldown"
#   For a single buy and sell:
#       max difference between subsequent buy and sell prices maximizes profit
#   For multiple:
#       combination of buy, sell pairs, where buy is not immediately after sell, s.t. the sum is largest than
#           than any other
#   Model the state transitions as a graph
#       nostock -> (holding, nostock) -> ((holding, cooldown), (holding, nostock)))
# Problem:
#   Find the maximum profit given an array of stock prices with above conditions
# Plan:
#   Model state transitions a graph
#   Depth first search to find path with the most profit
#       Carry a single max variable; update max when path is finished that has greater profit
#       For individual path carry profit state
#       Base case is (v + profit) when iteration reaches i + 1 == length

def max_profit_dfs(prices):
    maximum, length, graph = 0, len(prices), Graph()

    def search(i, prev, profit, purchase_price):
        nonlocal maximum

        if i == length:
            maximum = max(profit, maximum)
            return

        price = prices[i]

        for next in graph.neighbors(prev):
            if graph.is_sale(next, prev):
                gain = price - purchase_price
                if gain <= 0:
                    continue

                search(i + 1, next, profit + gain, None)
                continue

            if graph.is_purchase(next, prev):
                search(i + 1, next, profit, price)
                continue

            search(i + 1, next, profit, purchase_price)

    search(0, Graph.DRY_POWDER, 0, None)

    return maximum

class Graph:
    DRY_POWDER = 'DRY_POWDER'
    HOLDING = 'HOLDING'
    COOLDOWN = 'COOLDOWN'

    def __init__(self):
        self._GRAPH = {
            self.DRY_POWDER: [self.HOLDING, self.DRY_POWDER],
            self.HOLDING: [self.COOLDOWN, self.HOLDING],
            self.COOLDOWN: [self.DRY_POWDER]
        }

    def neighbors(self, STATE):
        return self._GRAPH.get(STATE)

    def is_sale(self, next, prev):
        return prev is self.HOLDING and next is self.COOLDOWN

    def is_purchase(self, next, prev):
        return prev is self.DRY_POWDER and next is self.HOLDING


# Understanding:
#   As discussed above, there are 3 possible states to be in at any point in time
#       HOLDING, COOLDOWN, DRY_POWDER
#   Insight: All we have to do is track the best way to get to each state at price i
#       The best way to get to any state at price i will both
#           i. provide maximum profit at end of iteration i.e. max(COOLDOWN, DRY_POWDER)
#           ii. provide enough information at every price i to deteminat the best scenarios for price i + 1
#   Since we are iterating from left to right and the above Adjacency Graph points to next states
#       we need to invert the graph to get _previous_ states:
#           DRY_POWDER: [DRY_POWDER, COOLDOWN]
#           HOLDING: [HOLDING, DRY_POWDER]
#           COOLDOWN: [HOLDING]
# Plan:
#   dry_powder[n] = max(dry_powder[n-1], cooldown[n-1])
#   holding[n] = max(dry_powder[n-1] - price[n], holding[n-1])
#   cooldown[n] = holding[n-1] + price[n]

def max_profit_dp(prices):
    if not len(prices):
        return 0

    powder, holding, cooldown = 0, -prices[0], float('-inf')

    for i, price in enumerate(prices):
        if i == 0:
            continue

        powder, holding, cooldown = max(powder, cooldown), max(powder - price, holding), holding + price

    return max(powder, cooldown)

# Problem: given an array of prices, buy and sell once to maximime profit
#   return 0 if no profit can be made
# Understanding:
#   (NO_STOCK) -> (NO_STOCK, HOLDING) -> ((NO_STOCK, HOLDING), (HOLDING, SOLD))
#   Brute Force:
#       iterate from left to right over every price i,
#           iterate from left to right for each j > i,
#               calc the max price[j] - price[i]
#   State machine:
#       no_stock[i] = no_stock[i - 1]
#       holding[i] = max(-price[i] + no_stock[i-1], holding[i-1])
#       sold[i] = holding[i-1] + price[i]
#   Insight:
#       Selling at price i exhausts all possible sales
# Plan:
#   iterate from left to right over every price i
#       maintain the min price
#       maintain the max sale
#   return the max sale

def max_profit_single_transaction_dp(prices):
    min_price, profit = prices[0], 0

    for i, price in enumerate(prices):
        if i is 0:
            continue

        profit = max(profit, price - min_price)
        min_price = min(min_price, price)

    return profit

def max_profit_single_transaction_dp_states(prices):
    holding, sold = -prices[0], 0

    for i, price in enumerate(prices):
        if i is 0:
            continue

        sold = max(sold, price + holding)
        holding = max(holding, -price)

    return sold
