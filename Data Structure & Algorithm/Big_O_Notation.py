def fact(n):
    product = 1
    for i in range (n):   #faster than second one  9 microsecond
        product =product * (i+1)
    return product
print("Factorial one :", fact(5))

def fact2(n):    #less faster 15 microsecond
    if n==0:
        return 1
    else:
        return n * fact2(n-1)
print("factorial 2 :", fact2(5))

                       # !----(  Big 0 Notation in Comes to Play)----!
import matplotlib.pyplot as plt
import numpy as np

def constant_algo(items):   #constant complexity
    result = items[0] * items[0]
    print (result)

constant_algo([5, 6, 6, 8])

x = [2, 4, 6, 8, 10, 12]

y = [2, 2, 2, 2, 2, 2]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Constant Complexity')
plt.show()

def linear_algo(items):     #linear Complexity
    for item in items:
        print(item)

linear_algo([4, 5, 6, 8])

x = [2, 4, 6, 8, 10, 12]

y = [2, 4, 6, 8, 10, 12]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()


def quadratic_algo(items):  #Quadratic Complexity
    for item in items:
        for item2 in items:
            print(item, ' ' ,item)

quadratic_algo([4, 5, 6, 8])


                       # Space Complexity
def return_squares(n):
    square_list = []
    for num in n:
        square_list.append(num * num)

    return square_list

nums = [2, 4, 6, 8, 10]
print(return_squares(nums))