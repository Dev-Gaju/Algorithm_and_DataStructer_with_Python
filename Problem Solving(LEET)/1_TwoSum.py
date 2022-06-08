# import requests
# import sys
#
# response = requests.get(sys.argv[1])
# print(response.status_code, response.content)

def TwoSum(num, target):   #complexity (O(n^2)
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i]+ num[j]== target:
                return [i,j]
        return []

"""
Total Combination will be n(n-1)//2.
we can used hash map to find best solution,
"""


# num=[2,1,3,4,11,13,7]
# target= 9
#
# print(TwoSum(num,target))


""" Hash Map for better complexity """
def TwoValueSum(num, target):
    lib={}
    for i, n in enumerate(num):
        if n in lib:
            return (lib[n], i)
        lib[target-n]= i
    return

num=[2,1,3,4,11,13,7]
target= 9

print(TwoValueSum(num,target))