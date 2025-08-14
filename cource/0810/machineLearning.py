# 机械学习百分之95的问题都在scikit-learn
# 模型最终的表现，有随机性，随机性来源：数据集、模型
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import neighbors
import sklearn

# importing the dataset
from sklearn.datasets import load_breast_cancer
data = datasets.load_iris()
X, y = data.data, data.target
train_x, test_x, train_y, test_y = train_test_split(X, y)

#
# model = neighbors.KNeighborsClassifier(n_neighbors= 1)
# model.fit(train_x, train_y)
# predictions  = model.predict(test_x)
# print("1 - KNN的预测结果", (test_y == predictions).sum(), len(test_x))
#
# model = neighbors.KNeighborsClassifier(n_neighbors= 3)
# model.fit(train_x, train_y)
# predictions  = model.predict(test_x)
# print("3 - KNN的预测结果", (test_y == predictions).sum(), len(test_x))
#
# model = neighbors.KNeighborsClassifier(n_neighbors= 5)
# model.fit(train_x, train_y)
# predictions  = model.predict(test_x)
# print("5 - KNN的预测结果", (test_y == predictions).sum(), len(test_x))


data = load_breast_cancer()
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']


# looking at the data
print(label_names)
print(labels)

from sklearn.model_selection import train_test_split

# splitting the data
train, test, train_labels, test_labels = train_test_split(features, labels,
                                    test_size = 0.33, random_state = 42)

from sklearn.naive_bayes import GaussianNB

# initializing the classifier
gnb = GaussianNB()

# training the classifier
model = gnb.fit(train, train_labels)

# making the predictions
predictions = gnb.predict(test)

# printing the predictions
print(predictions)