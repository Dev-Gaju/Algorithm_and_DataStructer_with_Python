def threeSum(nums):

    res =[]
    nums.sort()

    length = len(nums)

    for i in range(length-2):   #-2 means two pointer

        if i>0 and nums[i]== nums[i-1]:  #i shoudn't be reppiting
            continue
        l =i+1
        r = length-1

        while l<r:
            total = nums[i]+nums[l]+nums[r]
            if total < 0:   #-2,-1,0
                l =l+1
            elif total >0:
                r=r-1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while  l <r and nums[l]==nums[l+1] :                   #l and r should not be reppiting
                    l =l+1
                while  l <r and nums[r]==nums[r-1] :                   #l and r should not be reppiting
                    r =r-1

                l=l+1
                r=r-1
    return res


values = [-1,0,1,2,-1,-4]


print(threeSum(values))




