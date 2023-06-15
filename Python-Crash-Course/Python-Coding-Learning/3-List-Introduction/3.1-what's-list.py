#3.1 列表是什么，列表可以装任何元素，这些元素之间彼此没有任何关系
Motorcycle=['honda','kawasaki','suzuki','yamaha','voge']
#如果让Python将列表打印出来，则将打印列表的内部展示，包括方括号，输出：['honda','kawasaki','suzuki','yamaha','voge']
# print(Motorcycle)

#3.1.1访问列表元素
#列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置（索引）告诉Python即可
print(Motorcycle[0])#本行意为访问列表的第一个元素；这样就仅仅只返回该元素，而不包括方括号。
print(Motorcycle[1].title()) #在访问列表的第一个元素的基础上，将首字母大写；曾犯错误：“str.title() takes no arguments (1 given)”，即无需传参

#3.1.2索引是从0而不是1开始
print(Motorcycle[-1].title())#python特殊语法，基于“-1”可以访问列表的最后一个元素，同理“-3”访问的就是倒数第三个元素；常用于不知道最后列表长度的情况下，输出最后一个元素；

# 3.1.3使用列表中的各个值
message=f"my first Motorcycle was a {Motorcycle[0].title()}."#f:字符串组合函数；
print(message)
#或者换种方式
print(f"my first Motorcycle was a {Motorcycle[0].title()}.")