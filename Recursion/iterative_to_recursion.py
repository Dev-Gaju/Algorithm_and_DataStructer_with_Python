# def nbDivisor(n):
#     count =0
#     i=1
#     while i<=n:
#         if n % i ==0:
#             count +=1
#         i +=1
#     return count
#
# print(nbDivisor(12))


# Now Recursion transform

# def Nbdivisors(n ,count=0, i=1):
#     if i >n :
#         return count
#     else:
#         if n % i ==0:
#             count += 1
#         i +=1
#         return Nbdivisors(n, count, i)
# print(Nbdivisors(12))


#for loop condition

def NBdivisors(n):
    count =0
    for i in range(1, n+1):
        if n % i ==0:
            count +=1
    return count

print(NBdivisors(12))


#again recursion
# def NBDivisors(n, count =0, i=1):
#     if i>n :
#         return count
#     else:
#         if n % i ==0:
#             count +=1
#         return NBDivisors(n, count, i+1)
# print(NBDivisors(12))


