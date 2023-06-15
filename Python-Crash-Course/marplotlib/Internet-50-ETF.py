# 中概互联50-六月记录折线图
# matplotlib中有很多可用的模块，我们使用pyplot模块
import matplotlib.pyplot as plt
import numpy as np
day = [65, 66, 67, 68, 69]
networth = [0.7541, 0.8541, 0.9541, 0.8541, 0.7541]
#生成图表
plt.scatter(day, networth)
# plt.plot(day, networth)

#设置横坐标为day，纵坐标为networh，标题为每日净值记录更新
plt.xlabel('Day')
plt.ylabel('Networth')
plt.title('Networth Dayily correspondence')
#设置纵坐标刻度
plt.yticks([0, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50])

#设置填充选项：参数分别对应横坐标，纵坐标，纵坐标填充起始值，填充颜色（可以有更多选项）
# plt.fill_between(day, networth, 0, color = 'green')

#显示图表
plt.show()