#4.1 遍历整个列表
Motorcycle=['honda','kawasaki','suzuki','yamaha','voge','ducati']
for M in Motorcycle:#注意不要忘掉冒号和缩进，曾出错误：“SyntaxError: expected ':'”
    print(M)

#4.1.1 深入研究循环
#略

#4.1.2在for循环中执行更多操作
for M in Motorcycle:
    print(f"{M.title()},is a good Motorcycyle.")

#4.1.3在for循环结束后执行一些操作
#即在for循环外，执行某条代码，略