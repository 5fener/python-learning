# list和tuple有什么区别
list是[],tuple是{}；list可以增删改查，tuple是固定不可变；list速度更慢，内存占用更多
# dict为什么查询速度快
因为dict是哈希计算，键值对直接进行操作，空间换时间，O(1);
# == 和 is 有什么区别
==是值，is是对象，判断true or false
# for 和 while分别适合什么场景
for知道循环次数，while不知道循环次数但知道什么时候停止
# 函数为什么要有return
将函数的结果传递出来，需要结果就用return