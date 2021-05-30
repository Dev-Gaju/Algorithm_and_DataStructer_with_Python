
fibonacci_catch ={}
def memoizasion(n):
    if n in fibonacci_catch :
        return fibonacci_catch[n]

    if n==1:
        value =1
    if n==2:
        value =2
    if n >2:
        value = memoizasion(n-1) + memoizasion(n-2)
    fibonacci_catch[n] = value
    return value

for n in range(1, 100):
    print(n, memoizasion(n))
