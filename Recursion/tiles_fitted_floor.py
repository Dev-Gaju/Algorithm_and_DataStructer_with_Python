"""
Place a tiles on 1xm into a floor size nxm
Q: How many ways we can do that, suppose floor is 4,2 and tiles is 1x2

A: Two  ways we can place tiles , V & H. and V & H can helps to do that in 5 ways thinks,
if first is V then rest of the V & H mixed
if first is H then rest of is also be H & V

Base case discussion: If n=m(2=2) then tiles can place with two way V and H
n<m , so 1<2 then tiles could be fitted one time
it can be solved by using dybanic programming by less complexity
"""


def placeTiles(n, m):
    if n == m:
        return 2
    if n < m:
        return 1

    vertical = placeTiles(n - m, m)
    horizontal = placeTiles(n - 1, m)

    total_tiles = horizontal + vertical
    return total_tiles


print(placeTiles(2, 4))
