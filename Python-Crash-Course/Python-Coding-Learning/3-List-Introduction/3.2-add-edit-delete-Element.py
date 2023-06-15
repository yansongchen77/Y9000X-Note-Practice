#3.2 修改、添加、删除元素
Motorcycle=['honda','kawasaki','suzuki','yamaha','voge']

#3.2.1-修改列表元素：目前列表的第一个元素是'honda'
print(Motorcycle[0])
Motorcycle[0]='ducati'#将其改为ducati
print(Motorcycle[0])#查看修改是否生效；

#3.2.2在列表中添加元素
#(1)在列表末尾添加元素
Motorcycle[0]='honda'#将其改回为honda
Motorcycle.append('ducati')#appen()函数，可以将元素添加到列表末尾；
print(Motorcycle)

#（2）在列表中插入元素
Motorcycle.insert(5,'cf')#insert()函数，可以将元素插入到任意位置，后续元素均右移一个位置；
print(Motorcycle)

# (3)在列表中删除元素
#（3.1）使用Del语句删除元素（适用场景：明确知道删除元素在列表中的位置时）
del Motorcycle[0]
print(Motorcycle)
#(3.2)使用方法pop()删除元素（适用场景：删除元素，并接着使用值，类似栈）
Motorcycle.insert(0,'honda')#曾出错误：'builtin_function_or_method' object is not subscriptable（可下标）；只有对象才可以使用[]
poped_Motorcycle=Motorcycle.pop()#pop()默认删除列表末尾的元素，也就是()中无任何传参的情况下
print(Motorcycle)
print(poped_Motorcycle)
#(3.3)弹出列表中任何位置处的元素
Motorcycle.append('ducati')
first_owned=Motorcycle.pop(0)#pop()函数中传参列表索引，即可弹出列表中任何位置处的元素
print(f"The first motorcycle I owned was a {first_owned.title()}.")
#（3.4）根据值删除元素
Motorcycle.insert(0,'honda')
Motorcycle.remove('honda')#remove()函数基于传参的形式去删除列表元素,但只删除第一个指定的值，如果出现多次，需要使用循环（for）来删除；
print(Motorcycle)
#使用remove()删除元素时也可接着使用它的值：
too_expensive='ducati'
Motorcycle.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensice for me.")#\n 表示换行转义符号
