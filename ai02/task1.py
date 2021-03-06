# Decision tree classifier implementation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def calculate():
    df = pd.read_csv('iris.csv')
    # df['petal.width'].plot.hist()
    # plt.show()
    # sns.pairplot(df, hue='species')
    # plt.show()
    all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
    all_classes = df['species'].values
    (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7,                                                                                random_state=1)
    dtc = DecisionTreeClassifier(random_state=0, ccp_alpha=0.01)
    dtc.fit(train_inputs, train_classes)
    print("Score is " + str(dtc.score(test_inputs, test_classes)))
    clf = SVC(random_state=0)
    clf.fit(train_inputs, train_classes)
    plot_confusion_matrix(clf, test_inputs, test_classes)
    plt.show()
    # from the graphic we can see:
    # setosa - no mistakes
    # versicolor - no mistakes
    # virginica was confused with versicolor 1 time

    # pruning
    path = dtc.cost_complexity_pruning_path(train_inputs, train_classes)
    print(path)
    ccp_alphas, impurities = path.ccp_alphas, path.impurities
    plt.figure(figsize=(10, 6))
    plt.plot(ccp_alphas, impurities)
    plt.xlabel("effective alpha")
    plt.ylabel("")
    # plt.show()
    clfs = []
    for ccp_alpha in ccp_alphas:
        dtc = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
        dtc.fit(train_inputs, train_classes)
        clfs.append(dtc)
    acc_scores = [accuracy_score(test_classes, clf.predict(test_inputs)) for clf in clfs]
    tree_depths = [clf.tree_.max_depth for clf in clfs]
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.plot(ccp_alphas[:-1], acc_scores[:-1])
    plt.xlabel("effective alpha")
    plt.ylabel("Accuracy scores")
    # plt.show()

def main():
    calculate()

if __name__=="__main__":
    main()
