def oscillate(start: int, end: int):
    """ sinh ra (yield) lần lượt x rồi -x trong khoảng range(start, end)."""
    for x in range(start, end):
        yield x
        yield -x
        """ví dụ:"""
for n in oscillate(-3,5):
     print(n, end=' ')
