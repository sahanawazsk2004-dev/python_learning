#recursion = function call it self to solve problem 
#real ex- mirror ke aage mirror,factorial ,fibonaci series

"""
fibonaci series-
next result is sum of before two number
       0 1 1 2 3 5 8 13
index   0 1 2 3 4 5 6 7
             0+1 = 1
              1+1 = 2
               1+2 = 3 so on...

fib(0)=0
fib(1)=1
fib(2)=1
fib(3)=2
fib(n)= fib(n-2)+fib(n-1)



"""
# in recursin -> base case require 
def fib(n):
    #base case of recursion
    if(n == 0 or n == 1):
        return n

    return  fib(n-2) + fib(n-1)
print(fib(9))

#print(fib(45)) -> it show blank but functio call hota rehta hai,big number ke liye crores tak function call hota hai

#manually
fib(6)
fib(4) + fib(5)
fib(2)+fib(3)+fib(3)+fib(4)
fib(0)+fib(1)+fib(1)+fib(2)+fib(3)+fib(4)
0+1+1+fib(0)+fib(1)+fib(3)+fib(4)
0+1+1+0+1+fib(1)+fib(2)+fib(4)
0+1+1+0+1+1+fib(0)+fib(1)+fib(4)
0+1+1+0+1+1+0+1+fib(2)+fib(3)
0+1+1+0+1+1+0+1+fib(0)+fib(1)+fib(3)
0+1+1+0+1+1+0+1+0+1+fib(1)+fib(2)
0+1+1+0+1+1+0+1+0+1+1+fib(0)+fib(1)
0+1+1+0+1+1+0+1+0+1+1+0+1
