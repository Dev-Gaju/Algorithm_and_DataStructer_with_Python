def SubarraySum(nums, k):


    """
    calculate those value which sum is 7 it can be 5 number or it can be 7 number.
    like 1+2+4=7 or 1+4+2=7
    :param nums:
    :param k:
    :return:
    """

    sumdict = {0:1}   #make dictionary with key 0
    n =len(nums)
    count =0
    s=0


    for num in nums:
        s +=num
        if s-k in sumdict:
            count += sumdict[s-k]
            if s in sumdict:
                sumdict[s] +=1
            else:
                sumdict[s]=1
    return count

nums=[3,4,7,2,-3,1,4,2,1]
k=7
print(SubarraySum(nums,k))