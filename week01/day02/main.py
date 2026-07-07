#day02 条件语句、循环

#----练习1 判断奇偶数----
num = int(input("请输入一个数字："))
if num % 2 == 0:
    print("这是偶数")
else:
    print("这是奇数")
#----练习2 成绩等级(条件，多个分支)----
score = int(input("请输入成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
#----练习3 简单登录(条件，and 运算符)----
username = input("请输入用户名：")
password = input("请输入密码：")
if username == "admin" and password == "123456":
    print("登陆成功")
else:
    print("登陆失败")
#----练习4 1 到 100 求和(for 循环)----
num = 0
for i in range(1, 101):
    num += i
print("1到100的和为:", num)
#----练习5 猜数字(while 循环 + 条件)----
import random
target = random.randint(1, 100)
while True:
    guess = int(input("在1-100内猜测一个数字:"))
    if guess == target:
        print("恭喜你，猜对了！")
    elif guess < target:
        print("猜小了")
    else:
        print("猜大了")
#----练习6 打印乘法表(双重 for 循环)----
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {i*j}", end="\t")
    print()