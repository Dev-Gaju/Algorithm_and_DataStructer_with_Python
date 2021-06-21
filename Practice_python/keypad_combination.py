def KeypadCombination(key, i=0):
    keypad = ["+", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    if i == len(key):
        return [' ']
    else:
        key_value = KeypadCombination(key, i+1)
        output = [ ]
        for value in keypad[int(key[i])]:
            for combination in key_value:
                output.append(value+combination)

        return output

a=KeypadCombination('234')
print(len(a))
print(a)


