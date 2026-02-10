def rotateLeft(d, arr):

    for i in range(d):
        arr.append(arr.pop(0))
    return arr
