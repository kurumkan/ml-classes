import pandas as pd

def predictRow(sl, sw, pl, pw):
    if pl > 4.9:
        return "virginica"
    elif pw < 1:
        return "setosa"
    else:
        return "versicolor"

def calculate():
    df = pd.read_csv('iris.csv')
    points = 0
    for i, row in df.iterrows():
        sl = row['sepal.length']
        sw = row['sepal.width']
        pl = row['petal.length']
        pw = row['petal.width']
        species = row['species']

        prediction = predictRow(sl, sw, pl, pw)
        if prediction == species:
            points += 1

    total_rows = len(df)
    print("accuracy is " + str(points / total_rows))
    print("Total rows: " + str(total_rows))
    print(df.groupby("species").size())



def main():
    calculate()

if __name__=="__main__":
    main()

