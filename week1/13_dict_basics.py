# #字典基础
# student = {"name":"13nnk","age":24,"major":"AI"}#重点是花括号{}表示键值对
# print(student["name"])
# print(student["age"])

# student["grade"] = "研一"
# student["age"] = 25
# print(student)

# for key in student:
#     print(key,"=",student[key])
#     print("keys:", list(student.keys()))
#     print("values:", list(student.values()))
#     print("items:", list(student.items()))
# contacts = {}
# contacts["张三"] = "13800000001"
# contacts["李四"] = "13800000002"
# contacts["王五"] = "13800000003"

# name = input("输入名字查号码：")
# if name in contacts:
#     print(name,"的号码是：", contacts[name])
# else:
#     print("查无此人")

#用字典存成绩，循环找最高分

scores = {"张三": 85, "李四":92,"王五":78}

best_name =""
best_score = 0

for name in scores:
    if scores[name] > best_score:
        best_name = name
        best_score = scores[name]
        

print("最高分:",best_name,best_score,"分")