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
values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
limit = 25
min_val = 1500

def item_is_in_knapsack(it, knapsack):
    for i in knapsack:
        if i == it:
            return True
    return False


def end_state(knapsack):
    sum_val = 0
    sum_wei = 0
    for i in knapsack:
        sum_val = sum_val + values[i]
        sum_wei = sum_wei + weights[i]
    if sum_wei <= limit and sum_val > min_val:
        return True
    else:
        return False

def knapsack_is_full(knapsack):
    sum_wei = 0
    for i in knapsack:
        sum_wei = sum_wei + weights[i]

    return sum_wei >= limit

def dfs():
    stack = [[]]
    while True:
        if not stack:
            return False

        knapsack = stack.pop()

        if end_state(knapsack):
            print("We have  found a solution!")
            print(knapsack)
            return True


        if not knapsack:
            knapsack_max = -1
        else:
            knapsack_max = max(knapsack)

        for i in range(knapsack_max+1, num_items):
            if not item_is_in_knapsack(i, knapsack) and not knapsack_is_full(knapsack):
                son = copy(knapsack)
                son.append(i)
                stack.append(son)

start = time.time()
dfs()
end = time.time()
print("The total time [ms] of the algorithm is: ")
print(end - start)


# Difference between BFS and DFS
# BFS - first goes across elements on the same level
# queue states
## 1.[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# 2. [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]
# DFS goes down the branch
# stack states
# 1.[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# 2. [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]


# BFS speed
# 0.005537968577588811
# DFS speed
# 0.002531766891479492
# DFS is faster!