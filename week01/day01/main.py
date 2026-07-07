#day01 变量、数据类型、输入输出

#----练习1 输出你的名字----
print("张三")

#----练习2 输入年龄----
age = input("请输入你的年龄: ")
print("你的年龄是:", age)

#----练习3 计算十年后年龄----
age = input("请输入你的年龄: ")
ten_years_later = int(age) + 10
print("你十年后的年龄是:", ten_years_later)

#----练习4 摄氏度转华氏度----
celsius = float(input("请输入摄氏度："))
fahrenheit = celsius * 9/5 + 32
print("华氏度是:", fahrenheit)

#----练习5 两数相加----
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
result = num1 + num2
print("两数之和是：", result)