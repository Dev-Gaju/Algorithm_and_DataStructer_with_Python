num = -3030238
sign = -1 if num < 0 else 1
num *= sign
reverse_number = 0

while num > 0:
    digits = num % 10
    reverse_number = (reverse_number * 10) + digits
    num //= 10
reverse_number *= sign
print(reverse_number)


### String Reverse with Recursion

def Reverse_string(A, idx):
    if idx == 0:
        print(A[0])
        return
    print(A[idx], end=" ")
    Reverse_string(A, idx - 1)


A = "ABCD"
Reverse_string(A, len(A) - 1)

# another
nums = 12345
print(int(str(nums)[::-1]))
