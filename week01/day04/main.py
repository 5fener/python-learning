#day04 函数

#参数、返回值、局部变量

#----练习1 判断是否成年----
def is_adult(age):
    if age>= 18:
        return True
    else:
        return False

age = int(input("请输入年龄: "))
if is_adult(age):
    print("该用户已成年")
else:
    print("该用户未成年")

#----练习2 函数改写通讯录----
contacts = {}

def add_contact():
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    contacts[name] = phone
    print("联系人已添加")
def show_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"姓名: {name}, 电话: {phone}")
    else:
        print("通讯录为空")
def main():
    while True:
        print("\n--通讯录--")
        print("1. 添加联系人")
        print("2. 查看所有联系人")
        print("3. 退出")
        choice = input("请选择操作: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            print("感谢使用通讯录!")
            break
        else:
            print("无效选择")
main()
#----练习3 四则运算计算器----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "除数不能为 0"
    return a / b

def main():
    while(True):
        print("\n--四则运算计算器--")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 退出")
        choice = input("请选择操作: ")
        if choice == "1":
            a = float(input("请输入第一个数: "))
            b = float(input("请输入第二个数: "))
            print(f"结果: {add(a, b)}")
        elif choice == "2":
            a = float(input("请输入第一个数: "))
            b = float(input("请输入第二个数: "))
            print(f"结果: {subtract(a, b)}")
        elif choice == "3":
            a = float(input("请输入第一个数: "))
            b = float(input("请输入第二个数: "))
            print(f"结果: {multiply(a, b)}")
        elif choice == "4":
            a = float(input("请输入第一个数: "))
            b = float(input("请输入第二个数: "))
            print(f"结果: {divide(a, b)}")
        elif choice == "5":
            print("感谢使用计算器!")
            break
        else:
            print("无效选择")
            
main()