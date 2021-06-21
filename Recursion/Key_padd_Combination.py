# here used hashMap

def rec (keys, keypad, i, combination, output ):
    if i == len(keys):
        output.append(''.join(combination))
    else:
        for character in keypad[int(keys[i])]:
            combination.append(character)
            rec(keys, keypad, i+1, combination, output)
            combination.pop()

def keypad_combination(keys):
    output =[]
    keypad =["+", ".", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    rec(keys, keypad, 0, [], output)
    return output
a = keypad_combination("794")
print(a)


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
