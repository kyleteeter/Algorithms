#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max_profit = None
    for x in range(len(prices) -1):
        for y in range(x + 1, len(prices)):
            profit =  prices[y] - prices[x]
            if not max_profit:
                max_profit = profit
            elif max_profit < profit:
                max_profit = profit
    return max_profit
            
  
#   Loop through array
# store current min price
# store current max price
# compair


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))