def decorator():
    print("decorator is work")
    yield "Abdulbosit"
    yield "Abdulboriy"
    yield "Dilshod"


def plus_task(x, b):
    print("plus task is work")
    yield x + b


def minus_task(y, b):
    print("minus task is work")
    if y >= b:
        yield a - b


for i in decorator():
    print(i)
for j in plus_task(4, 5):
    print(j)
for a in minus_task(10, 7):
    print(a)


