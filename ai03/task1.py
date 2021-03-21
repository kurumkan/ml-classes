# 1
# how can state search tree be represented?
# it can be represented as json, or as hashmap
# {
#   "key": "a",
#   "val": [],
#   "children": [
#       {
#           "key": "b"
#            "val": ["book"],
#           .....
#       }
#       ....
#   ]
# }
#
#

# 2 explaining each line:
# importing external modules
from copy import copy
import time

num_items = 11
items = ["clock",
         "painting - nature",
         "painting - portrait",
         "radio",
         "laptop",
         "lamp",
         "silver cutlery",
         "porcelain cups",
         "bronze statue",
         "leather bag",
         "vacuum cleaner"]
# prices
values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
limit = 25
min_val = 1500

# check if item is in knapsack
def item_is_in_knapsack(it, knapsack):
    for i in knapsack:
        if i == it:
            return True
    return False

# check if we are at the end state
def end_state(knapsack):
    sum_val = 0
    sum_wei = 0
    # calculate sum of values and weights
    for i in knapsack:
        sum_val = sum_val + values[i]
        sum_wei = sum_wei + weights[i]
    # if sum of weight is less or equal the limit and if value sum is more than 1500 should return true
    if sum_wei <= limit and sum_val > min_val:
        return True
    else:
        return False


# bfs implementation
def breadth_first_search():
    queue = [[]]
    while True:
        if not queue:
            return False

        knapsack = queue.pop(0)
        # check if knapsack is in end state - if yes return True
        if end_state(knapsack):
            print("We have  found a solution!")
            print(knapsack)
            return True

        # find max val in the knapsack
        if not knapsack:
            knapsack_max = -1
        else:
            knapsack_max = max(knapsack)

        for i in range(knapsack_max+1, num_items):
            # if item is not in knapsnak - append it and put to to the queue
            if not item_is_in_knapsack(i, knapsack):
                son = copy(knapsack)
                son.append(i)
                queue.append(son)

# running bfs algorithm and measure the time
start = time.time()
breadth_first_search()
end = time.time()
print("The total time [ms] of the algorithm is: ")
print(end - start)


# c
# queue for first 2 loop iterations:
# 1.[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# 2. [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]