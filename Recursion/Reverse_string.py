def string_reverse(str):
    if str =='':
        return ''
    else:
        return string_reverse(str[1:]) + str[0]

a = string_reverse("Abcdef")
print(a)

