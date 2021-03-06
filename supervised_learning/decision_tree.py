# Decision tree classifier implementation

import pandas as pd
import scipy.stats as stats

MIN = 0.00001

# get shuffled data
# train_data, test_data = np.array_split(pd.read_csv('./golf.csv').sample(frac=1).reset_index(drop=True), 2)
train_data = pd.read_csv('./golf.csv').sample(frac=1).reset_index(drop=True);

def dt(feat, hasOptions):
    result = {}
    if hasOptions:
        for option in train_data[feat]:
            dt(option, False)

    eClass = stats.entropy(train_data[feat].value_counts(), base=2)
    for i in train_data:
        1

    print(stats.entropy([5,9],[], base=2))
    # print(stats.entropy(train_data[feat].value_counts(), train_data["Outlook"].value_counts(), base=2))
    return result

def predictRow(outlook, temp, humidity, windy):
    tree = dt('Play Golf', False)
    print(tree)
    return 1

def calculate():
    prediction = predictRow("Sunny", "Mild", "Normal", "Weak")
    print(prediction)
    # points = 0
    # for i, row in test_data.iterrows():
    #     outlook = row['Outlook']
    #     temp = row['Temp']
    #     humidity = row['Humidity']
    #     windy = row['Windy']
    #     play = row['Play Golf']
    #     prediction = predictRow(outlook, temp, humidity, windy)
    #     if prediction == play:
    #         points += 1
    #
    # print("accuracy is " + str(points / len(test_data)))

def main():
    calculate()

if __name__=="__main__":
    main()
