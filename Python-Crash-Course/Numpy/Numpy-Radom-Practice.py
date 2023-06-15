#NumPy 是一个 Python包,它代表 “Numeric Python”。它是一个由多维数组对象和用于处理数组的例程集合组成的库。
import numpy as np

#打印输出Numpy的版本和配置信息；
# print(np.__version__)
# print(np.show_config())

#创建一个长度为10的空向量；
Z0=np.zeros(10)
print(Z0)

#如何找到任何一个数组的内存大小？
Z1=np.zeros((10,10))
print("%d bytes" % (Z1.size * Z1.itemsize))