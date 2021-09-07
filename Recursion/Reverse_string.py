def string_reverse(str):
    if str =='':
        return ''
    else:
        # print(str[0])
        print(str[1:])
        # print(str[0])
        return string_reverse(str[1:]) + str[0]
        # print(str[1:])
        # return a

a = string_reverse("abcdef")
print(a)

