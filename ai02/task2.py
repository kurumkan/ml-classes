# KNN implementation
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import plot_confusion_matrix

def compareK():
    df = pd.read_csv('iris.csv')
    all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
    all_classes = df['species'].values
    (train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)

    # building confusion matrix
    clf = SVC(random_state=0)
    clf.fit(train_inputs, train_classes)
    plot_confusion_matrix(clf, test_inputs, test_classes)
    plt.show()
    # confusion matrix - we can see only 1 mistake has been done
    # it was predicted that virginica but actually it was versicolor

    best_k = 0
    max_score = -1
    for k in range(3, 50, 2):
        score = getScore(k, train_inputs, train_classes, test_inputs, test_classes)
        print(score)
        if score > max_score:
            max_score = score
            best_k = k

    print("Best value of k = " + str(best_k))
    print("Best score = " + str(max_score))


# predicting
def getScore(k, train_inputs, train_classes, test_inputs, test_classes):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_inputs, train_classes)
    return knn.score(test_inputs, test_classes)

def main():
    compareK()

if __name__=="__main__":
    main()
