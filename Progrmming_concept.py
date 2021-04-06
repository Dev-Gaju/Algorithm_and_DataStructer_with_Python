# Find_the_largest_value
# largest_number = 0
# for number in [32, 23, 45, 11, 22, 49, 5, 79]:
#     if number > largest_number:
#         largest_number= number
#     print(largest_number, number)
#
# print(f"The largest Number is { largest_number} ")

# # find the smallest value


smallest_number = None
for number in [9, 23, 45, 11, 22, 49, 5, 79]:
    if smallest_number is None:
        smallest_number = number
    elif number < smallest_number :
        smallest_number = number
    print(smallest_number, number)

print(f"The Smallest Number is { smallest_number} ")