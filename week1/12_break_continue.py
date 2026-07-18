for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
for i in range(1, 11):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)