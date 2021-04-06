def slicer(word):
    if len(word) % 2 == 0:
        return 'even'
    else:
        return word[-2:]


mylist = ['ABCDE', 'AA', 'ADEW', 'WKLOP']
a = list(map(slicer, mylist))  # we are just calling the function not executing with brackets
print(a)  # map give logical result Like true or false and also take total value


# Filter Implementation
def check_even(nums):
    return nums % 2 == 0


number = [1, 2, 3, 4, 5, 6, 7, 8]
a = list(filter(check_even, number))  # filter give the value or map just say true or false
print(a)

                                    # Lambda Implementation!!! lambda work as anonymous function
result = list(map(lambda x: x ** 2, [1, 2, 3, 4]))  # two variable of map 0n is func other is list
print(result)

# nums = [11, 22, 33, 44, 55]
#
# r = list(filter(lambda x: x ** 2, nums))
# print(r)
