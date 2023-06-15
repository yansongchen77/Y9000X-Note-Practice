#3.3 组织列表（排序）
Motorcycle=['honda','kawasaki','suzuki','yamaha','voge','ducati']

#3.3.1使用方法sort（）对列表永久排序
Motorcycle.sort()#默认按照字母顺序排列
print(Motorcycle)

Motorcycle.sort(reverse=True)#按照字母顺序相反的顺序排列
print(Motorcycle)

#3.3.2使用函数sorted对列表临时排序
Motorcycle.sort()#恢复
print("\nHere is the Original list:")
print(Motorcycle)

print("\nHere is the sorted list:")
print(sorted(Motorcycle))

#如果需要按照字母顺序相反的顺序排列，则亦可以传递参数reverse=True
print("\nHere is the sorted list(Reverse version):")
print(sorted(Motorcycle,reverse=True))

print("\nHere is the Original list again:")
print(Motorcycle)
#在并非所有值都是小写时，按字母顺序排列列表要更为复杂，决定排列顺序时，有多种解读大写字母的方式，实际排列应该比该处更为复杂，本节仅为基础；

#3.3.3倒着打印列表(使用方法reverse（）)
Motorcycle.reverse()
print(Motorcycle)

#3.3.4确定列表的长度(使用函数len（）)
# len(Motorcycle),从函数的角度来说，列表是函数的参数，而方法的区别在于，是由列表（或者说对象）来调用方法；
print(len(Motorcycle))