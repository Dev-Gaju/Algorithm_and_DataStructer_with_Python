def rec (arr, i, phrase, output):
    if i ==len(arr):
        output.append(' '.join(phrase))
    else:
        for word in arr[i]:
            phrase.append(word)
            rec(arr, i+1, phrase, output)
            phrase.pop()
def phrases(arr):
    output = []
    rec(arr,0, [], output)
    return  output

n= [["John", "Gaju", "Abdul"],
    ["cock", "eat", "like"],
    ["Rice", "Burger", "chicken"]]
a = phrases(n)
print(a)



# method 2:
# def phrases(arr, i=0):
#   if i == len(arr):
#     return ['']
#   else:
#     fromNext = phrases(arr, i+1)
#     output = []
#     for word in arr[i]:
#       for phrase in fromNext:
#         output.append(word + (' ' if len(phrase) > 0 else '') + phrase)
#     return output
#
# n= [["John", "Gaju", "Abdul"],
#     ["cock", "eat", "like"],
#     ["Rice", "Burger", "chicken"]]
# a = phrases(n)
# print(a)