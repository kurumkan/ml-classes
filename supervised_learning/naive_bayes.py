# Naive Bayes implementation

import pandas as pd
import numpy as np

MIN = 0.00001

# get shuffled data
train_data, test_data = np.array_split(pd.read_csv('./iris.csv').sample(frac=1).reset_index(drop=True), 2)

def predictRow(sl, sw, pl, pw):
    classes = train_data.groupby(by=['species']).groups
    total_rows = len(train_data);

    p_class = {}
    for i in classes:
        total_of_class = classes[i].size
        p_class[i] = {
            'p_class': total_of_class / total_rows,
            'total_of_class': total_of_class
        }

    p_sl_class = {}
    for i in classes:
        intersection = train_data[(train_data['species'] == i) & (train_data['sepal.length'] == sl)]
        p_sl_class[i] = (len(intersection) or MIN) / p_class[i]['total_of_class']

    p_sw_class = {}
    for i in classes:
        intersection = train_data[(train_data['species'] == i) & (train_data['sepal.width'] == sw)]
        p_sw_class[i] = (len(intersection) or MIN) / p_class[i]['total_of_class']

    p_pl_class = {}
    for i in classes:
        intersection = train_data[(train_data['species'] == i) & (train_data['petal.length'] == pl)]
        p_pl_class[i] = (len(intersection) or MIN) / p_class[i]['total_of_class']

    p_pw_class = {}
    for i in classes:
        intersection = train_data[(train_data['species'] == i) & (train_data['petal.width'] == pw)]
        p_pw_class[i] = (len(intersection) or MIN) / p_class[i]['total_of_class']

    result = {}
    for i in classes:
        result[i] = p_sl_class[i] * p_sw_class[i] * p_pl_class[i] * p_pw_class[i] * p_class[i]['p_class']

    return max(result, key=result.get)

def calculate():
    points = 0
    for i, row in test_data.iterrows():
        sl = row['sepal.length']
        sw = row['sepal.width']
        pl = row['petal.length']
        pw = row['petal.width']
        species = row['species']
        prediction = predictRow(sl, sw, pl, pw)
        if prediction == species:
            points += 1

    print("accuracy is " + str(points / len(test_data)))

def main():
    calculate()

if __name__=="__main__":
    main()
