# KNN implementation
# For KNN training stage is completely skipped

import pandas as pd
import numpy as np

# get shuffled data
train_data, test_data = np.array_split(pd.read_csv('./iris.csv').sample(frac=1).reset_index(drop=True), 2)

def predictRow(sl_test, sw_test, pl_test, pw_test, k):
    # generate array of distances
    # sort up
    # get first k elements of sorted distances array
    # which species outnumber others?
    distances = []
    for i, row in train_data.iterrows():
        sl = row['sepal.length']
        sw = row['sepal.width']
        pl = row['petal.length']
        pw = row['petal.width']
        species = row['species']

        a = np.array([sl, sw, pl, pw])
        b = np.array([sl_test, sw_test, pl_test, pw_test])
        dist = np.linalg.norm(a - b)
        distances.append([dist, species])

    distances = np.array(distances)
    distances = distances[distances[:, 0].argsort()]
    first_k = distances[:k]
    first_k[first_k[:, 1].argsort()]
    print(first_k)
    print('-------------------')
    return first_k[0][1]

def calculate(k):
    points = 0
    for i, row in test_data.iterrows():
        sl = row['sepal.length']
        sw = row['sepal.width']
        pl = row['petal.length']
        pw = row['petal.width']
        species = row['species']
        prediction = predictRow(sl, sw, pl, pw, k)
        if prediction == species:
            points += 1
    print("K = " + str(k) + ", accuracy = " + str(points / len(test_data)))

def main():
    # for i in range(1, 10, 2):
    #     calculate(i)
    calculate(9)

if __name__=="__main__":
    main()
