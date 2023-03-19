"""
Have a rectangle(maze) now from starting box(0,0) we need to go last path(n,m).how many ways we go there.
Condition: we only can go down and right not left or upper.

Backtracking : when we used all possible approach then we can called it backtracking.

"""


def totalPath(i, j, n, m):
    if i == n or j == m:
        return 0
    if i == n - 1 & j == m - 1:
        return 1

    down_path = totalPath(i + 1, j, m, n)  # go down
    right_path = totalPath(i, j + 1, m, n)  # go right
    total_path = down_path + right_path
    return total_path


n = 3
m = 3
print(totalPath(0, 0, n, m))
