a = []
for i in range(5):
    ele = int(input())
    a.append((ele))
# print(a)

a.sort()
b=0
for i in range(len(a)-1):
     b += a[i]
print(b)
c=0
for i in range(1,len(a)):
     c += a[i]
print(c)

# 2nd one
nums = [int(x) for x in input().strip().split(' ')]
print(sum(nums) - max(nums), sum(nums) - min(nums))

#3rd One

lst = map(int,raw_input().strip().split(' '))
x = sum(lst)
print (x-(max(lst))), (x-(min(lst)))

# 4th one

