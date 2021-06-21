def make_sentence(arr, i, phrase, output):
    if i == len(arr):
        return output.append(' '.join(phrase))
    else:
        for char in arr[i]:
            phrase.append(char)
            make_sentence(arr, i+1, phrase, output)
            phrase.pop()

def sentence(arr):
    output = []
    make_sentence(arr, 0, [], output)
    return output

n= [["John", "Gaju", "Abdul"],
    ["cock", "eat", "like"],
    ["Rice", "Burger", "chicken"]]
print(sentence(n))