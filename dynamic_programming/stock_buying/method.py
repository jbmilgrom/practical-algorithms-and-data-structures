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

def max_profit_with_cooldown_dfs(prices):
    maximum, length, graph = 0, len(prices), CooldownGraph()

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

    search(0, CooldownGraph.DRY_POWDER, 0, None)

    return maximum

class CooldownGraph:
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

def max_profit_with_cooldown_dp(prices):
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
    if not len(prices):
        return 0

    holding, sold = -prices[0], 0

    for i, price in enumerate(prices):
        if i is 0:
            continue

        sold = max(sold, price + holding)
        holding = max(holding, -price)

    return sold

# Understanding:
#   buy low, sell high results in profit
#   can buy and sell multiple times
#   cannot hold more than one stock at a time
#   states:
#       (POWDER) -> (POWDER, HOLDING) -> ((POWDER, HOLDING), (POWDER, HOLDING))
#        P -> H -> P (and each can go back to self)
def max_profit_multiple_transactions(prices):
    if not len(prices):
        return 0

    powder, holding = 0, -prices[0]

    for i, price in enumerate(prices):
        if i == 0:
            continue

        powder = max(powder, holding + price)
        holding = max(holding, powder - price)

    return powder

# Understanding:
#   Can make at most two transactions
#   A transaction is a roundtrip: it occurs when stock is bought and sold
#   Note that the multiple transactions algo accrues profit indiscriminately
#   Now we need to cap transactions
#   Brute force DFS: we could model all the state changes and constrain paths based on 2 transaction cap
# Plan:
#   depth first search of the various states
#   track transactions
#   track max profit
#   when transaction limit is reached, stop searching and compare to previous max
def max_profit_two_transactions_dfs_recurse(prices):
    if not len(prices):
        return 0

    max_profit, graph = 0, BuySellGraph()

    def search(i, state, holding, profit, transactions):
        nonlocal max_profit

        if transactions == 2 or i == len(prices):
            max_profit = max(max_profit, profit)
            return

        for next in graph.neighbors(state):
            if graph.is_purchase(state, next):
                search(i + 1, next, prices[i], profit, transactions)
                continue

            if graph.is_sale(state, next):
                search(i + 1, next, None, profit + prices[i] - holding, transactions + 1)
                continue

            search(i + 1, next, holding, profit, transactions)

    search(0, graph.DRY_POWDER, None, 0, 0)

    return max_profit

def max_profit_two_transactions_dfs_stack(prices):
    graph = BuySellGraph()
    stack = [(graph.DRY_POWDER, 0, 0, 0)]
    max_profit = 0

    while len(stack):
        state, profit, transactions, i = stack.pop()

        if transactions == 2 or i == len(prices):
            max_profit = max(max_profit, profit)
            continue

        for next in graph.neighbors(state):
            price = prices[i]

            if graph.is_purchase(state, next):
                profit = profit - price

            if graph.is_sale(state, next):
                transactions += 1
                profit = profit + price

            stack.append((next, profit, transactions, i + 1))

    return max_profit


class BuySellGraph:
    DRY_POWDER = 'DRY_POWDER'
    HOLDING = 'HOLDING'

    def __init__(self):
        self._graph = {
            self.DRY_POWDER: [self.DRY_POWDER, self.HOLDING],
            self.HOLDING: [self.HOLDING, self.DRY_POWDER]
        }

    def neighbors(self, state):
        return self._graph.get(state)

    def is_purchase(self, prev, next):
        return prev is self.DRY_POWDER and next is self.HOLDING

    def is_sale(self, prev, next):
        return prev is self.HOLDING and next is self.DRY_POWDER
