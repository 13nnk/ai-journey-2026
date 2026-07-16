tasks = []
task1 = input("请输入第一个任务:")
tasks.append(task1)
task2 = input("请输入第二个任务:")
tasks.append(task2)
task3 = input("请输入第三个任务:")
tasks.append(task3)

print("今天共有",len(tasks),"个任务")

for task in tasks:
    print(task)