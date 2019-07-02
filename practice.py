def more_than_half(A):
    n = len(A)
    if n == 0:
        return -1

    m = int(n / 2)
    if A[0] == A[m]:
        return A[0]
    return -1


def recursive_inc(c, A):
    if A[c] < A[c+1]:
        return c
    else:
        return recursive_inc(c+1, A)
