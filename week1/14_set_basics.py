# 创建集合
skills = {"python","Git","Linear Algebra"}
print(skills)
# 集合也用花括号 {}，但里面只有值，没有键
# 集合的特点：元素不重复、没有顺序

skills.add("numpy")
print("添加后：",skills)

skills.discard("Git")
print("删除后：",skills)

# .add() — 往集合里加元素
# .discard() — 删除元素，如果不存在也不会报错
# 对比字典：字典用 student["key"] = value 添加，集合用 .add() 添加


math_skills = {"线性代数","微积分","概率论"}
code_skills = {"python","Git","Numpy"}
all_skills = math_skills | code_skills#并集
common = math_skills & code_skills #交集
print("并集：",all_skills)
print("交集",common)
# | — 并集，两个集合所有元素合在一起 
# & — 交集，两个集合共有的元素
# 这里没有共同元素，所以交集是空集合 set()

#用集合去重

numbers = [1,2,2,3,3,3,4,5,5]
unique = set(numbers)
print("原始:",numbers) 
print("去重:",unique) 
print("去重列表:",list(unique)) 
# set(numbers) — 把列表转成集合，重复的自动去掉
# list(unique) — 再转回列表
# 这就是集合最常用的场景：去重

