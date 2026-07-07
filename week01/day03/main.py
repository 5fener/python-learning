# day03 列表、元组、字典、集合

#----练习1 列表增删改查----
my_list = [1, 2, 3, 4, 5]
print("原始列表:", my_list)

# 增加元素
my_list.append(6)
print("添加元素后:", my_list)

# 删除元素
my_list.remove(3)
print("删除元素后:", my_list)

# 修改元素
my_list[0] = 10
print("修改元素后:", my_list)

# 查找元素
if 10 in my_list:
    print("找到了元素10")
else:
    print("没有找到元素10")

#----练习2 求列表平均值----
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
average = total/len(my_list)
print("列表平均值：", average)

#----练习3 学生成绩管理系统（字典）----
score = {"张三": 85, "李四": 90, "王五": 78}
name = input("请输入学生姓名：")
if name in score:
    print(f"{name}的成绩是：{score[name]}")
else:
    print("没有找到该学生")

#----练习4 统计字符串中每个字符出现次数（字典）----
text = input("请输入一个字符串")
count = {}
for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print("字符出现次数：", count)

#----练习5 列表去重（集合）----
num = [1, 2, 2, 3, 3, 4, 4, 5]
unique_num = list(set(num))
print("去重前的列表：", num)
print("去重后的列表：", unique_num)

#----练习6 坐标距离计算（元组拆包）----
point1 = (3, 4)
point2 = (7, 8)
x1, y1 = point1
x2, y2 = point2
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("两点间距离：", distance)

#----练习7 综合小练习简单通讯录----
contacts = {}
