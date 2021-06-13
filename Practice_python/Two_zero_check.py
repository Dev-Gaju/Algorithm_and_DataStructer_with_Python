

def Binary_value_check(n, bin, output):
    if n == 0:
        if bin.count('1') <=2:
             output.append( ' '.join(bin))

    else:
        bin.append('0')
        Binary_value_check(n - 1, bin, output)
        bin.pop()
        bin.append('1')
        Binary_value_check(n - 1, bin, output)
        bin.pop()



def check_value(n):
    output=[]
    Binary_value_check(n,[], output)
    return output

print(check_value(5))
