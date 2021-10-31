def fib(n):
if n==0:
   return 0
else:
   if n==1:
      return 1
   else:
      return fib(n-1)+fib(n-2)
a=int(input("enter any number"))
for i in range(a):
   result=fib(i)
   print(result)
