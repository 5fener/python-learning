# 文件操作、json

#----练习1 写文件并读取----
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("今天天气真好\n")
    f.write("适合学Python\n")

with open("text.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

#----练习2 逐行读取 + 行数统计----
with open("text.txt", "r", encoding="utf-8") as f:
    count = 0
    for line in f:
        count += 1
        print(f"第{count}行: {line.strip()}")
print(f"总行数: {count}")

#----练习3 用户输入保存到文件并追加----
with open("text.txt", "w", encoding="utf-8") as f:
    user_input = input("请输入要保存的内容：")
    f.write(f"{user_input}\n")
with open("text.txt", "a", encoding="utf-8") as f:
    user_input = input("请输入要追加的内容：")
    f.write(f"{user_input}\n")
with open("text.txt", "r", encoding="utf-8") as f:
    print("最后的内容:\n", f.read())

#----练习4 JSON 序列化与反序列化----
import json
person = {"name": "Alice", "age": 30, "city": "New York"}
# 字典 → JSON 字符串
json_str = json.dumps(person, ensure_ascii=False)
print("JSON 字符串：", json_str)
# JSON 字符串 → 字典
back = json.loads(json_str)
print("name:", back["name"])
print("age:", back["age"])

#----练习5 JSON 读写文件----
import json

students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False)
print("已保存到 students.json")

#----练习6 通讯录json版----