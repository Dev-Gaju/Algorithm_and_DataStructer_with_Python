num = -3030238
sign  = -1 if num <0 else 1
num *= sign
reverse_number = 0

while num >0:
    digits = num %10
    reverse_number = (reverse_number *10) + digits
    num //=10
reverse_number *= sign
print(reverse_number)