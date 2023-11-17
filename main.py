"""print("hello", "all", end=" ")
print("hi")
print(13 / 6)
print(format(13 / 6, ".3f"))
print(format(5 / 2, ".3f"))
hello = 2 + 3
hello1 = 3 + 4
hello = 4 + 7
print(hello)
a = 10
k = a
a = 6
print(a)
print(k)
a = 10
k = a
k = 6
print(a)
print(k)
b = 3
c = b
print(id(b), b)
print(id(c), c)
print(type(7 + 2j))
print(type(eval("2+4-1")))
print(40.0/10.00)"""
"""num = int(input("enter a number "))
if num > 0:
    print("entered number",num,"is positive")
elif num < 0 :
    print("entered number",num,"is negative")
else :
    print("entered number",num,"is zero")"""
""""a = int(input())
b = int(input())
c = int(input())
if a == b:
  if b == c:
     print("yes")

  else :
      print("no")"""
"""i = 1
while i <= 5:
  print(i)
  i += 1
print("end of loop")"""
"""num = int(input("enter a number"))
i = 1
sum = 0
while i <= num:
  sum += i
  i += 1
print("sum is",sum )"""
"""a = input("enter selection:")
while a != 'f' and a != 'c':
     a = input("please enter 'f' or 'c'")"""
"""numbers = [1,2,3,4]
print("original numbers ",numbers)
for i in range(len(numbers)):
  numbers[i] += 1
print("new numbers",numbers)"""
"""import math
num = int(input ("enter max limit:"))
for i in range(1,num+1):
  print(i , ":" ,math.sqrt(i))"""
"""lst1 =  [1,2,3,4,5]
lst2 = (lst1[::])
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))"""
"""n = int(input("enter a number:"))
if n%3 == 0 and n%5 == 0  :
  print("FIZZBUZZ")
elif n% 5 == 0 :
  print("BUZZ")
elif n%3 == 0 :
  print("FIZZ")
else :
  print(n,"is not divisible by 3 or 5)"""
"""name = input("enter your name:")
age = int(input("enter your age:"))
if age >= 18:
  print(name,"you r eligible for applying driving license")
else:
  print(name,"you r not eligible for applying driving license")"""
"""year = int(input("enter a four digit year:"))
if year % 100 == 0:
  
  if year % 400 ==0:
     leap = True
  else:
     leap = False
elif year % 4 == 0 :
  leap = True
else :
  leap = False
if leap == True:
  print(year,"leap year")
else:
  print(year,"not a leap year")
  """
"""for i in range(2,10,1):
  for j in range(1,i,1):
    print(j,end=" ")
  print()"""
"""a = True
b = False
c = False
if not a or b :
  print(1)
elif not a or not b and c:
  print(2)
elif not a or not b and not a:
  print(3)
else:
  print(4)"""
"""Serial_number = "hello"
print(Serial_number)

 



print('menu of simple calculator:')
print("1.addition")
print('2.subtraction')
print('3.multiplication')
print('4.division')
print('5.modulus')
print('6.exit')
ch = 0
while ch < 6:
        ch = int(input("enter choice from 1  to 6:"))
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
   if ch == 1:
       c = a+b
       print('sum is',c)

  elif ch == 2:
        c = a-b
        print('diffence is',c)

   elif ch == 3:
        c = a*b
        print('product is',c)

   elif ch == 4:
        c = a/b
        print('quotient is',c)

   elif ch == 5 :
        c = a%b
        print('remainder is',c)

   elif ch == 6: 
        print("exit")
   else:
       print("invalid choice")"""

"""def compute(func,x,y):
  for fun in func:
    print(fun(x,y))
def add(a,b) :
  return a+b
def mul(a,b):
  return a*b
lst = [add,mul]
compute(lst,15,20)"""


"""def outer(lst):
  newlist = []
  def even(num):
    if num % 2 == 0:
      return True
  for i in lst:
    if even(i) == True:
      newlist.append(i)
  print(newlist)

lst = [2,3,4,5,6,7,9,10]
outer(lst)"""


"""def outer():
  print("hi")
  def inner():
    print("hello")
  return inner

fun = outer()
fun()"""


"""def fib(n):
  x,y = 0,1
  for i in  range(n):
    x,y=y,x+y
    yield x
for i in fib(3):
  print(i)"""


"""def fib(n):
  x,y = 0,1
  for i in range(n):
    x,y=y,x+y
    yield x
def sq(n):
  for i in n:
    yield i**2
print(sum(sq(fib(5))))"""
