# def year(number):
#     num = number
#     mylist = []
#     for i in range(10):
#         mylist.append(num)
#         num -= 1
#
#     return mylist


num = 2022
mylist = [(num - i) for i in range(10)]
print(mylist)