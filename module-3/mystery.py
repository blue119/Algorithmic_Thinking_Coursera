
def mystery(arr, l, r):
    """@todo: Docstring for mystery.

    :arr: @todo
    :l: @todo
    :r: @todo
    :returns: @todo

    """
    if l > r: return -1

    m = (l + r)/2
    print m, l, r
    if arr[m] == m:
        return m
    elif arr[m] < m:
        return mystery(arr, m+1, r)
    else:
        return mystery(arr, l, m-1)

if __name__ == '__main__':
    arr = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 21, 22, 23]
    l = 0
    r = len(arr)
    print mystery(arr, l, r)

