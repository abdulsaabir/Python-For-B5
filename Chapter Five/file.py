# # import math
# # # # import random
# # from math impo/rt pow
import time
# # # # # r = random.randint(10,100000)
# # # # # f = random.uniform(1,1000)
# # # # # print(r)
# # # # # print(f)

# # # # # students = ['ilhaan mohamed', 'Asmo Abdullaahi', 'Xaawo Nuur', 'Nasteexo Cadow', 'Ahmed Siyaad', 'Mohamed Yusuf', 'Abdiraham Ahmed']
# # # # # c = random.choice(students)
# # # # # print(c)
# # # # # c = random.shuffle(students)
# # # # r = random.random()
# # # # print(r)

# # # def Divide(a,b):
# # #     if b == 0:
# # #         result = 'Cannot divide by zero'
# # #     else:
# # #         result = a/b
# # #     print(result)
# # #     return result

# # # result = Divide(1,0)
# # # print(result)

# # # c = math.ceil(100.5)
# # # f = math.floor(100.5)
# # # r = round(100.5)
# # # print('ceil', c)
# # # print('floor', f)
# # # print('round', r)

# # # p = math.pow(2,4)
# # # print(p)
# # # s = math.sqrt(64)
# # # print(s)
# # # t = math.trunc(232.2212)
# # # print(t)
# # f = math.factorial(4)
# # print(f)
# p = pow(2,4)
# print(p)


def CountSeconds(seconds):
    if seconds <= 0:
        return 'End'
    while seconds > 0:
        print(seconds)
        seconds -= 1
        time.sleep(1)
CountSeconds(30)