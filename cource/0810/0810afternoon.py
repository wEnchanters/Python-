from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import neighbors
from sklearn.datasets import fetch_20newsgroups

data = datasets.load_iris()
X, y = data.data, data.target


# model = linear_model.LogisticRegression()
# model.fit(X,y)
# print(model)

# 数据切分 25% 样本划分为测试集
train_x, test_x, train_y, test_y = train_test_split(X, y)
# 真实标签
print("真实标签", test_y)
# 模型初始化，人工设置的参数叫做超参数，模型参数可以从训练集学习到的
model = linear_model.LogisticRegression(max_iter = 1000)
model.fit(train_x, train_y)
# 预测结果
predictions = model.predict(test_x)
print("预测结果", predictions)
print("线性拟合的预测结果", (test_y == predictions).sum(), len(test_x))

# 模型最终的表现，有随机性，随机性来源：数据集、模型
model = tree.DecisionTreeClassifier()
model.fit(train_x, train_y)
predictions  = model.predict(test_x)
print("决策树预测结果", (test_y == predictions).sum(), len(test_x))


# 模型最终的表现，有随机性，随机性来源：数据集、模型
model = neighbors.KNeighborsClassifier(n_neighbors= 1)
model.fit(train_x, train_y)
predictions  = model.predict(test_x)
print("1 - KNN的预测结果", (test_y == predictions).sum(), len(test_x))

model = neighbors.KNeighborsClassifier(n_neighbors= 3)
model.fit(train_x, train_y)
predictions  = model.predict(test_x)
print("3 - KNN的预测结果", (test_y == predictions).sum(), len(test_x))

model = neighbors.KNeighborsClassifier(n_neighbors= 5)
model.fit(train_x, train_y)
predictions  = model.predict(test_x)
print("5 - KNN的预测结果", (test_y == predictions).sum(), len(test_x))

# 需要背诵决策树


from fastapi import FastAPI

app = FastAPI()

# 2. 定义一个 API 端点 (路径操作装饰器)
@app.get("/")  # 当有 GET 请求访问根路径 "/" 时，执行下面的函数
async def read_root():
    # 3. 返回 JSON 响应
    return {"message": "Hello, FastAPI World!"}

@app.get("/hello")
async def say_hello():
    return {"greeting": "你好，掘金的朋友们！"}


model = fetch_20newsgroups(subset='all')
print(model.data[0])
print(model.target[0])
print(model.target_names)
