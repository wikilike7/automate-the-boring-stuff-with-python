# while loop
# spam = 0
# while spam < 5:
#     print('I am spam')
#     spam += 1


# while True:
#     print('Please type your name: ')
#     name = input()
#     if name == 'your name':
#         break  # 跳出循环
# print('Thank you!')


# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('What is your password: ')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted')


for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i += 1


# 高斯
total = 0
i = 0
while i < 101:
    total += i
    i += 1
print(total)


for i in range(0, 11, 2):  # 从0开始，不超过11，步长是2
    print(i)


for n in range(10, -1, -2):  # 负的步长
    print(n)


# import module
import random, sys, os, cmath
for i in range(5):
    print(random.randint(1, 10))


while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()


# exise
# 1. True, False
# 2. and or not
# 3. 省略，太多了，不写了， 记住是短路径判断
# 4. False False True False False True
# 5. > == < >= <= !=
# 6. == =
# 7. while 和 for
# 8. if if else
# 9.
    spam = 1
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings!')
# 10. ctrl + c
# 11. break是跳出循环，continue是流程跳至代码块的头部重新执行
# 12，没区别
# 13.
    # for
    for i in range(1, 10):
        print(i)
    # while
    n = 1
    while n < 10:
        print(n)
        n += 1
# 14. import bacon
# 15. round()是对浮点数取四舍五入的值， abs()是对参数取绝对值














