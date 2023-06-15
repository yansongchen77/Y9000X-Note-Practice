#4.3 创建数值列表
for value in range(1,5):#快速创建数值列表
    print(value)
#调用函数range（）的时候，也可以仅放一个参数，则会从0开始，例如range（6），会输出0，1，2，3，4，5

#4.3.2使用range（）创建数字列表
numbers=list(range(1,6))#基于list（）函数调用range（）函数，生成列表；
print(numbers)

#range函数还可以指定步长，一般为第三个参数
even_numbers=list(range(2,11,2))
print(even_numbers)

# 使用range函数理论上可以生成任何数集
squares=[]#生成空列表
for s in range(1,11):
    s=s**2#**表示乘方运算；
    squares.append(s)
print(squares)
#从简洁代码的角度，上述乘方列表，还可以下述方式创建
# for s in range(1,11):
#     squares.append(s**2)
# print(squares)

#4.3.3对数字列表执行简单的统计运算
print(min(squares))
print(max(squares))
print(sum(squares))

#4.3.4列表解析
#列表解析将for循环和创建新元素的代码合并在一起，并自动附加新元素
p_numbers=[value**2 for value in range(1,11)]
print(p_numbers)
#values**2:表达式，用于生成要存储到列表中的值
# for循环：用于给表达式提供值；
#方括号：表示生成的值存储到列表中；