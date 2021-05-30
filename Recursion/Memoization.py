
fibonacci_catch ={}

def fibonacci(n):
    #check the value then return it
    if n in fibonacci_catch:
        return fibonacci_catch[n]

    #compute the value cache it and return it
    if n==1:
        value=1
    elif n==2:
        value = 1
    elif n>2 :
        value = fibonacci(n-1) + fibonacci(n-2)

    #catch it then return it
    fibonacci_catch[n] = value
    return value

for  n in range(1, 500):
    print(n, fibonacci(n))

            #Seconds tools with module

# from functools import lru_cache
# @lru_cache(maxsize=1000)
# def fibonacci(n):
#     #chect the input is an integar and positive number
#     if type(n) !=int:
#         raise TypeError("n must be an positive number")
#     if n<1:
#         raise ValueError("n must be an positive integer")
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n>2 :
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# for n in range(1, 500):
#     print(n, fibonacci(n))