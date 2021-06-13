def rec (n , bin, output):
    if n ==0:
        if bin.count('0') <=2:
            output.append(''.join(bin))
    else:
        bin.append('0')
        rec(n-1, bin, output)
        bin.pop()
        bin.append('1')
        rec(n-1, bin,output)
        bin.pop()

        #if want to used loop instead of that function

        # for bit in ['0', '1']:
        #     bin.append(bit)
        #     rec(n-1, bin, output)
        #     bin.pop()


def binaryNumbers(n):
    output =[]
    rec (n, [], output)
    return output


print(binaryNumbers(5))