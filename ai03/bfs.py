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



def breadth_first_search():
    queue = [[]]
    while True:

        if not queue:
            return False

        knapsack = queue.pop(0)

        if end_state(knapsack):
            print("We have  found a solution!")
            print(knapsack)
            return True


        if not knapsack:
            knapsack_max = -1
        else:
            knapsack_max = max(knapsack)

        for i in range(knapsack_max+1,num_items):
            if not item_is_in_knapsack(i, knapsack):
                son = copy(knapsack)
                son.append(i)
                queue.append(son)


start = time.time()
breadth_first_search()
end = time.time()
print("The total time [ms] of the algorithm is: ")
print(end - start)
