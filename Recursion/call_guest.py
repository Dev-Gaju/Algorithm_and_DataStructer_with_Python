"""
Invite guest and tell the ways with pair and single to call them in parities.
Suppose you invite two guest , you can call them single or call them double -> there is two ways.
"""


def callGuest(n):
    if n <= 1:
        return 1
    single_call = callGuest(n - 1)
    double_cal = (n - 1) * callGuest(n - 2)
    total_guest = single_call + double_cal
    return total_guest


print(callGuest(2))
