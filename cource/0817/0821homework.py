import torch
import torch.nn as nn












import torch
import numpy as np
import matplotlib.pyplot as plt

# # 1. 生成模拟数据 (与之前相同)
# # np.random生成的是numpy数组
# X_numpy = np.random.rand(100, 1) * 10
# y_numpy = 2 * X_numpy + 1 + np.random.randn(100, 1)
# X = torch.from_numpy(X_numpy).float()
# y = torch.from_numpy(y_numpy).float()
#
# print("数据生成完成。")
# print("---" * 10)
#
# # 生成一个randon的pytorch张量，这个张量需要梯度计算require_grad，类型 dtype=torch.float
# a = torch.randn(1, requires_grad=True, dtype=torch.float)
# b = torch.randn(1, requires_grad=True, dtype=torch.float)
#
# # 损失函数，均方差mse(mean square error)
# loss_fn = torch.nn.MSELoss()
#
# # 优化器
# optimizer = torch.optim.SGD([a,b], lr = 0.01)
#
# num_epochs = 100
# for epoch in range(num_epochs):
#     y_pred = a * X + b
#
#     loss = loss_fn(y_pred, y)
#
#     # 清空梯度
#     optimizer.zero_grad()
#     # 计算梯度
#     loss.backward()
#     # 更新参数
#     optimizer.step()
#     if epoch % 100 == 0:
#         print(f"{epoch} / {num_epochs} : {loss.item():.4f}")
#
# print("\n训练完成！")
#
# a_learned = a.item()
# b_learned = b.item()
# print(f"拟合的斜率 a: {a_learned:.4f}")
# print(f"拟合的截距 b: {b_learned:.4f}")
# print("---" * 10)
#
# # 6. 绘制结果
# # 使用最终学到的参数 a 和 b 来计算拟合直线的 y 值
# with torch.no_grad():
#     y_predicted = a_learned * X + b_learned
#
#
#
# plt.figure(figsize=(10, 6))
# plt.scatter(X_numpy, y_numpy, label='Raw data', color='blue', alpha=0.6)
# plt.plot(X_numpy, y_predicted, label=f'Model: y = {a_learned:.2f}x + {b_learned:.2f}', color='red', linewidth=2)
# plt.xlabel('X')
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)
# plt.show()

# import numpy as np
# import torch.nn as nn
# # 1. 生成模拟数据 (与之前相同)
# # np.random生成的是numpy数组
# X_numpy = np.random.rand(100, 1) * 10
# y_numpy = 2 * X_numpy + 1 + np.random.randn(100, 1)
# X = torch.from_numpy(X_numpy).float()
# y = torch.from_numpy(y_numpy).float()
#
# print("数据生成完成。")
# print("---" * 10)
#
# # 线性回归模型
# model  = nn.Linear(in_features = 1, out_features=1)
# # 定义优化器 (随机梯度下降)
# # model.parameters() 会自动找到模型中需要优化的参数（即a和b）
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01) # lr 是学习率
# loss_fn = nn.MSELoss()
# num_epochs = 100
# for epoch in range(num_epochs):
#     y_pred = model(X)
#
#     loss = loss_fn(y_pred, y)
#
#     # 清空梯度
#     optimizer.zero_grad()
#     # 计算梯度
#     loss.backward()
#     # 更新参数
#     optimizer.step()
#     if epoch % 100 == 0:
#         print(f"{epoch} / {num_epochs} : {loss.item():.4f}")
#
# # 打印最终学到的参数
# # model.weight 是斜率a， model.bias 是截距b
# print("\n训练完成！")
# a_learned = model.weight.item()
# b_learned = model.bias.item()
# print(f"拟合的斜率 a: {a_learned:.4f}")
# print(f"拟合的截距 b: {b_learned:.4f}")
#
#
# # 将模型切换到评估模式，这在训练结束后是好习惯
# model.eval()
#
# # 禁用梯度计算，因为我们不再训练
# with torch.no_grad():
#     y_predicted = model(X).numpy() # 使用训练好的模型进行预测
# # 绘图
# plt.figure(figsize=(10, 6))
# plt.scatter(X_numpy, y_numpy, label='Raw data', color='blue', alpha=0.6)
# plt.plot(X_numpy, y_predicted, label=f'Model: y = {a_learned:.2f}x + {b_learned:.2f}', color='red', linewidth=2)
# plt.xlabel('X')
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)
# plt.show()



