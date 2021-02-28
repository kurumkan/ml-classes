from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

def processTipsData():
    totals = [16.99,    10.34,  21.01,  23.68,  24.59   ]
    tips =   [1.01,     1.66,   3.50,   3.31,   3.61    ]
    sexes =  ['Female', 'Male', 'Male', 'Male', 'Female']
    TipsDataSet = list(zip(totals, tips, sexes))
    df = pd.DataFrame(data=TipsDataSet, columns=['total_bill', 'tip', 'sex'])
    df.to_csv('tips.csv', index=False, header=True)
    print("Mean value in 'total_bill' column: " + str(df['total_bill'].mean()))
    print("Maximum value in 'tip' column: " + str(df['tip'].max()))


def main():
    processTipsData()

if __name__=="__main__":
    main()

