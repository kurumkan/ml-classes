# Naive bayes implementation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

def calculate():
    df = pd.read_csv('iris.csv')
    all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
    all_classes = df['species'].values
    (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7,                                                                                random_state=1)

    gnb = GaussianNB()
    gnb.fit(train_inputs, train_classes)
    pred = gnb.fit(train_inputs, train_classes).predict(test_inputs)
    print("Accuracy = " + str(accuracy_score(test_classes, gnb.predict(test_inputs))))
    print("Number of mislabeled points out of a total %d points : %d" % (train_classes.shape[0], (test_classes != pred).sum()))

    # confusion matrix
    # setosa - 0 mistakes
    # versicolor - 1 mistake with virginica
    # virginica - 2 mistakes with versicolor
    plot_confusion_matrix(gnb, test_inputs, test_classes)
    plt.show()

    # comparing accuracies of all 3:
    # 0.9555555555555556 for decision tree
    # 0.9777777777777777 for knn
    # 0.9333333333333333 is of naive bayes
    # Knn performed the best

def main():
    calculate()

if __name__=="__main__":
    main()
