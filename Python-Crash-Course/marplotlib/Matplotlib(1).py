# 参考文档：https://zhuanlan.zhihu.com/p/388287863
import matplotlib.pyplot as plt
import numpy as np

# 在 Matplotlib 中，图形（类plt.Figure的一个实例）可以被认为是一个包括所有维度、图像、文本和标签对象的容器。
# 维度（类plt.Axes的一个实例）即为图像，一个有边界的格子包括刻度和标签，最终还有我们画在上面的图表元素。
# 变量名fig：图形对象；
# 变量名ax：维度变量。
# 下列注释代码的主要表示：绘制一个简单的正弦函数图形：
# fig = plt.figure()
# ax = plt.axes()
x = np.linspace(start=0, stop=10, num=1000) #numpy的linspace()函数组主要是用于创建数值序列的工具，生成结构和Numpy类似的均匀分布的数值序列，通过订一均匀间隔创建数值序列，主要是三个参数：
# 间隔起始点、终止端、以及指定分隔值总数（包含起始点和终止点）：
# start：起始点；
# stop：终止点；
# num：间隔的分隔值总数（包含起始点和终止点）
# 最终函数返回间隔类均匀分布的数值序列，一般来说，实际调用时无需显示指定参数名称，可以通过参数位置直接匹配，例如：np.linspace(0, 100, 5)

# pyplot的plot()函数主要是用于绘图，可以绘制点和线，可参考：https://zhuanlan.zhihu.com/p/258106097
# 主要有两个参数，一般是横坐标和纵坐标，
# 最简单的plot函数示例如下：
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x));

# plt.plot(x, np.sin(x - 0), color='blue', linestyle='-')        # 通过颜色名称指定
# plt.plot(x, np.sin(x - 1), color='g', linestyle='--')           # 通过颜色简写名称指定(rgbcmyk)
# plt.plot(x, np.sin(x - 2), color='0.75', linestyle='-.')        # 介于0-1之间的灰阶值
# plt.plot(x, np.sin(x - 3), color='#FFDD44', linestyle=':')     # 16进制的RRGGBB值，字符串形式去处理
# plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB元组的颜色值，每个值介于0-1
# plt.plot(x, np.sin(x - 5), color='chartreuse'); # 能支持所有HTML颜色名称值

# # 从简洁代码的角度来说，也可以使用下列内容
# plt.plot(x, x + 0, '-g')  # 绿色实线
# plt.plot(x, x + 1, '--c') # 天青色虚线
# plt.plot(x, x + 2, '-.k') # 黑色长短点虚线
# plt.plot(x, x + 3, ':r');  # 红色点线

#pyplot库中的show()函数，主要用于显示图表 
plt.show()