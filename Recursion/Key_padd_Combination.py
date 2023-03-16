# here used hashMap
# time complexity is (4^n)
def printComb(keys, idx, combination):
    if idx == len(keys):
        print(combination)
        return
    current_char = keys[idx]
    mapping = keypad[int(current_char)]
    for i in range(len(mapping)):
        printComb(keys, idx + 1, combination + mapping[i])
        i += 1


key = "103"
keypad = ["+.", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TU", "VWX", "YZ"]
comb = " "
printComb(key, 0, comb)













# method 2:
# def keypadCombinations(keys, i=0):
#     keypad = ["+", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
#     if i == len(keys):
#         return ['']
#     else:
#         fromNext = keypadCombinations(keys, i + 1)
#         # print(fromNext)
#         output = []
#         # print(keys[1])
#         # print(i)
#         print(keypad[int(keys[i])])
#
#
#         for letter in keypad[int(keys[i])]:
#             # break
#             for combination in fromNext:
#                 output.append(letter + combination)
#         return output
# a = keypadCombinations("2794")
# print(a)
