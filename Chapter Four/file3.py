# # # # write a function that prints numbers from 1 to N 
# # # def PrintNumbers(end):
# # #     for i in range(1,end + 1):
# # #         print(i)


# # # PrintNumbers(19)


# # # write a function that prints ALL EVEN NUMBERS of N 
# # # from 1 to N
# # # def PrintEvenNumbers(n):
# # #     for i in range(1,n):
# # #         if i % 2 == 0:
# # #             print(i)

# # def PrintEvenNumbers(n):
# #     for i in range(1,n,2):
# #         print(i)

# # PrintEvenNumbers(51)


# # write a function that prints multiplication table of
# # of N number
# # output would look like this: if N is 3
# # 4 x 1 = 3
# # 4 x 2 = 6
# # 4 x 3 = 9 
# # 4 x 4 = 12
# def multiplication(n):
#     for i in range(1,13):
#         # n x i = nxi
#         # print(n, ' x ', i, ' = ', i * n)
#         print(f'{n} x {i} = {i*n}')
# multiplication(10)


# 4 = 4 + 3 + 2 + 1 = 10
# write a function that returns the count from 1 to N 
# USE WHILE LOOP

def returnTotal(n):
    total = 0
    start = 1
    while start <= n :
        total += start
        start  += 1
    return total
x  = returnTotal(4)
print(x)
x= returnTotal(x)
print(x)
x = returnTotal(x)
print(x)