
n = int(input().strip())
arr = [1 if int(temp)>0 else -1 if int(temp)<0 else 0 for temp in input().strip().split(' ') ]
print("{0:.6f}".format(arr.count(1)/n))
print("{0:.6f}".format(arr.count(-1)/n))
print("{0:.6f}".format(arr.count(0)/n))




# p = 0
# n = 0
# z = 0
# for i in range(len(values)):
#     if values[i]  < 0:
#         n +=1
#     elif values[i] > 0:
#         p += 1
#     else:
#         z +=1
#
# print("{0:6f}".format(p/len(values)))
# print("{0:6f}".format(n/len(values)))
# print("{0:6f}".format(z/len(values)))