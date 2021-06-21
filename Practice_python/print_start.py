def print_star(star):
    if star == '':
        return ''
    else:
        print(star)
        return print_star(star[1:]) + star[0]

print_star("*****")