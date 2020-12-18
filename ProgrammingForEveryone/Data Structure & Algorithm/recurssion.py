import datetime


def recursion(val):
    emptyArray = 0

    for i in val:
        emptyArray = emptyArray + i
    return emptyArray


start = datetime.datetime.now()
print(recursion([1, 4, 5, 7, 8]))
end = datetime.datetime.now()

tf = end - start
print(tf.seconds)
