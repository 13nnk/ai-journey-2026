def greet():
    print("hello,AI World")

greet()
# 给函数传入参数
def greet_name(name):
    print("Hellp," + name + "!")
greet_name("13nnk")
greet_name("Python")

# 让函数返回结果
def add(a,b):
    result = a + b
    return result
answer = add(3,5)
print("计算结果：",answer)

#默认参数
def power(base, exponent=2):
    result = base ** exponent
    return result

print("3 的平方：", power(3))
print("3 的三次方：", power(3, 3))

# 函数和循环组合
def sum_numbers(n):
    total = 0

    for number in range(1, n + 1):
        total = total + number

    return total

answer = sum_numbers(5)
print("1 到 5 的总和：", answer)

# 计算长方形面积
def rectangle_area(length, width):
    area = length * width
    return area

result = rectangle_area(4, 3)
print("长方形面积：", result)