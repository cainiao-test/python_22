#分子
a = 2

# 分母
b = 1

s = 0

for i in range(20):
    s = a / b + s
    a, b = (a + b), a
print(s)
