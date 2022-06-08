
# n = int(input("enter the number of element : "))
#
# a =[]
# b =[]
#
# for  ele in range(0, n):
#     val = int(input())3
#     a.append(val)
# print(a)


# Below line read inputs from user using map() function
n = int(input("Enter number of elements : "))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print(a)