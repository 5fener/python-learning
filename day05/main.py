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
    print("最后的内容：", f.read())