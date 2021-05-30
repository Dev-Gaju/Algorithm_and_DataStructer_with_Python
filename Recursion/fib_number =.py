
def fib_number(number):
    if number==1:
        return 1
    elif number==2:
        return 1

    return  fib_number(number-1) + fib_number(number-2)

for n in range(1, 10):
    print(n, fib_number(n))
fib_number(5)


            # Factorial Implementation
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))
