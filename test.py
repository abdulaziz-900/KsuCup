# value = 5
# def main():
#     show_double(value)
# def show_double(number):
#     result = number * 2
#     value = 6
#     print(result)
# main()
# main()


#
# value = 5
# def main():
#     show_double(value)
# def show_double(number):
#     result = number * 2
#     global value
#     value = 6
#     print(result)
# main()
# main()

#
# my_list=[1,2,3,4,5]
# print(my_list[0], my_list[1], my_list[-2], my_list[-1])
# x=[10,20,30,10]
# od=0
# even=0
# for i in range(len(x)):
#     if i%2==0:
#         even+=x[i]
#     else:
#         od+=x[i]
# if od==even:
#     print("True")
# else:
#     print("False")

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(2,80)
# print(numbers)
# numbers = [[1, 2, 4],
# [0, 5, 0],
# [9, 7, 0]]
# # printing lists row by row
# for row in range(len(numbers)):
#     for x in range(row):
#         print(x, end=",")
#     print()
# string=" "
# print(string.isspace())
# dict={"Ali":1122,"Ahmad":2233}
# # del dict["Ahmad"]
# # print(dict)
# print(dict.values())
# print(dict)
# people = {111: {'name': 'John', 'age': '27', 'sex': 'Male'},
# 222: {'name': 'Mary', 'age': '22', 'sex': 'Female'},
# 333: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'employed':'No'}}
# del  people[222]
# print(people)
# phonebook = {'Chris':'555-1111', 'Katie':'555-2222',
# 'Joanne':'555-3333'}
# Names = list(phonebook.keys())
# Numbers = list(phonebook.values())
# print(Names)
# myset = set(['one', 'two', 'three'])
# myset.add("four")
# print(myset)
# setA=([1,2,3,4])
# setb=([1,2])
# print(setb<=setA)


# a = [2,4,5,2,7,8,2,6]
# b = a[:]
# for x in b:
#     if x in range(2,5):
#      a.remove(x)
# print(a)

# def main():
#  try:
#     num1 = int(input('Enter a number: '))
#     num2 = int(input('Enter another number: '))
#     result = int(num1 / num2)
#     print(num1, 'divided by', num2, 'is', result)
#  except ZeroDivisionError:
#         print('Cannot divide by zero.')
#  except ValueError:
#         print('Please Enter Numbers')
#  finally:
#      print("Thanks for using our program.")
#
# main()


# class Bank:
#     def __init__(self, name, type, balance, currency):
#      self.clientName = name
#      self.accountType = type
#      self.__balnace = balance
#      self.currency = currency
#     def __str__(self):
#      return self.clientName+","+self.accountType+","+str(self.__balnace)+","+self.currency
#     def getbalance(self):
#         return self.__balnace
# account1 = Bank("Ali","Personal",1000,"SR")
# account2 = Bank("Ahmad","Personal",1100,"SR")
# print(account2)
# print(account2 is account1) # return True if the two instances are the same
#



# import re
# password = "123456Aa"
# reg = "^(?=.*[A-Z])[A-Za-z0-9]{6,8}$"
# pat = re.compile(reg)
# x = re.search( pat, password)
# if(x):
#     print("Valid")
# else:
#     print("inValid")

#
# l1 = ["python", "Java", "c++"]
# obj = enumerate(l1)
# print(list(obj))
# for item in enumerate(l1):
#  print(item)
# for count, item in enumerate(l1, 100):
#  print(count, item)

# def arg_printer(**kwargs):
#  print(kwargs)
# arg_printer(var1=5, var2=6, var3=7, var4=9)
# add_one = lambda x: x + 1
# print(add_one(2))


# numbers = (1, 2, 3, 4)
# numbers1 = (5, 6, 7, 8)
# result = map(lambda x,y: x%2==0, numbers,numbers1)
# print(list(result))

# string_it = ["processing", "strings", "with", "map"]
# list(map(str.capitalize, string_it)) # ['Processing', 'Strings', 'With', 'Map']
# list(map(str.upper, string_it)) # ['PROCESSING', 'STRINGS', 'WITH', 'MAP']
# list(map(str.lower, string_it))


# seq = [0, 1, 2, 3, 5, 8, 13]
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result)) # odd numbers
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))




#
# objects = [0, 1, [], 4, 5, "", None, 8]
# clean_objects = list(filter(None, objects))
# print(clean_objects)
vec = [2, 4, 6]
# [3*x for x in vec]

# vec = [2, 4, 6]
# [3*x for x in vec if x > 3]
list1=[]
# for i in vec:
#         list1.append(3*i)
# print(list1)
# for x in range(len(vec)):
#     if vec[x]>3:
#         vec[x]=vec[x]*3
# print(vec)
# l1 = ["python", "Java", "c++"]
# obj = enumerate(l1)
# print(list(obj))
# for item in enumerate(l1):
#   print(item)
# for count, item in enumerate(l1, 100):
#   print(count, item)
# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
# # [x*y for x in vec1 for y in vec2]
# result=[]
# for x in vec1:
#     for i in vec2:
#         result.append(x*i)
# print(result)
#
# print(format(1.5,'.0%'))\
# seta=([2,4,6,8,10])
# N=2
# def mullti(a,b):
#  for i in a:
#      if i%b==0:
#          return True
#  return False
# r=list(seta)
# print(mullti(seta,N))
# olddict={'Mon':1000,'Sat':4000,'Tue':3200,'Fri':5000}
# newdict={'Sun':2310,'Mon':900,'Wed':800,'Fri':4500}
# def merge(old,new):
#     r={}
#     for i in new:
#         for j in old:
#             if i[0]==j[0]:
# vec1=[2,4,6]
# vec2=[4,3,-9]
# lista=[]
# # for x in vec1:
# #     for y in vec2:
# #         lista.append(x*y)
# # print(lista)
# for x in vec1:
#     for y in vec2:
#        lista.append(x+y)
# print(lista)
#
# y='google.com'
# dict1={}
# for i in y:
#     if i in dict1:
#         dict1[1]=dict1[i]+1
#     else:
#         dict1[i]=1
# print(dict1)
#
# def list2(li):
#     x=set(li)
#     return x
# listr=[1,2,3,3,4]
# print(list2(listr))
#
#
#

# def clear(oR):
#     for i in oR:
#       oR[i].clear()
#
#     return oR
#
# ot={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# print(clear(ot))
#
#
#

x=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
def d(list1,subject):
    listw=[]
    for i in list1:
        if subject in i:
         listw.append(i[subject])
    return listw

print(d(x,'Science'))











