def sumOfDigit(n):
    if n<0:
        return sumOfDigit(-n)
    if n < 10:
        return n
    else:
        a=sumOfDigit(n//10)
        print(a)
        return a + n % 10

a=sumOfDigit(2334)
print(a)

# tail recursive:
# def sumOfDigts(n, acc=0):
# 	if n < 0:
# 		return sumOfDigts(-n)
# 	elif n < 10:
# 		return n+acc
# 	else:
# 		return sumOfDigts(n//10, acc+n%10)