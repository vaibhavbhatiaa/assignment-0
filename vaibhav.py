Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> val1 = 5
>>> val2 = 7
>>> res = val1 + val2
>>> print(res)
12
>>> val1 = 4
>>> val2 = 7
>>> res = val1 - val2
>>> print(res)
-3
>>> val1 = 20
>>> val2 = 6
>>> res = val1 / val2
>>> print(res)
3.3333333333333335
>>> val1 = 9
>>> val2 = 2
>>> res = val1 % val2
>>> print(res)
1
def maximum(a, b, c):
  
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest

a = 15.5
b = 15.34
c = 13
print(maximum(a, b, c))
15.5
