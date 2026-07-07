#day06 面向对象

#----练习1 简单类----
class Cat:
    def __init__(self, name):
        self.name = name
    def Meow(self):
        print(f"{self.name}: 喵喵！")

cat1 = Cat("小花")
cat2 = Cat("小黑")

cat1.Meow()
cat2.Meow()

#----练习2 学生类----
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def display_info(self):
        print(f"学生：{self.name}, 分数：{self.score}")
    def is_pass(self):
        if self.score >= 60:
            print(f"{self.name}及格了")
        else:
            print(f"{self.name}没及格")
    
student1 = Student("张三", 85)
student2 = Student("李四", 55)

student1.display_info()
student1.is_pass()

student2.display_info()
student2.is_pass()

#----练习3 银行账户类----
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}存款{amount}元，余额：{self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            print(f"{self.owner}取款{amount}元，余额：{self.balance}")
        else:
            print("余额不足或取款金额无效")
    def show_balance(self):
        print(f"{self.owner}的余额： {self.balance}元")

acc1 = BankAccount("张三", 1000)
acc1.show_balance()
acc1.deposit(500)
acc1.withdraw(200)
acc1.show_balance()

#----练习4 用面向对象重写通讯录----

#----练习5 图书管理类----

#----练习6 学生管理系统----