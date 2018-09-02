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

    search(0, Graph.NO_STOCK, 0, None)

    return maximum

class Graph:
    NO_STOCK = 'NO_STOCK'
    HOLDING = 'HOLDING'
    COOLDOWN = 'COOLDOWN'

    def __init__(self):
        self._GRAPH = {
            self.NO_STOCK: [self.HOLDING, self.NO_STOCK],
            self.HOLDING: [self.COOLDOWN, self.HOLDING],
            self.COOLDOWN: [self.NO_STOCK]
        }

    def neighbors(self, STATE):
        return self._GRAPH.get(STATE)

    def is_sale(self, next, prev):
        return prev is self.HOLDING and next is self.COOLDOWN

    def is_purchase(self, next, prev):
        return prev is self.NO_STOCK and next is self.HOLDING

