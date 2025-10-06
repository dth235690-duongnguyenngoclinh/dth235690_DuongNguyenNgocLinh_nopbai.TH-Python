i, j, k = 5,7,3
if i < j and j < k:
    print(i, j, k)
elif i < k and k < j:
    print(i, k, j)
elif j < i and i < k:
    print(j, i, k)
elif j < k and k < i:
    print(j, k, i)
elif k < i and i < j:
    print(k, i, j)
else:
    print(k, j, i)