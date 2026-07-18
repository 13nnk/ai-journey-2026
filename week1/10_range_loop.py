# M1 Day3 -rang()循环练习
for number in range(5):
    print(number)

for number in range(1,6):  #也可以自己设起点，1到6之前停不包括6的五个数
    print(number)    

for number in range(0,10,2):#自己设置步长，起点为0终点为10步长为2
    print(number)

#while 循环练习
count = 0   
while count < 3:
    print("当前 count 是:",count)
    count = count + 1

count = 3
while count > 0:
    print("倒计时：",count)
    count=count - 1
print("发射")