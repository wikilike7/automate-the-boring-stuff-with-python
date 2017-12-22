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
# 2. 















