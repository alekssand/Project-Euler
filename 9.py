squares_to_500 = []

for i in range(1,501):
    squares_to_500.append((i, i**2))

st5 = dict(squares_to_500)
st5_rev= dict([(b, a) for a, b in squares_to_500])

for c in range(335, 501):
    sq = st5[c]
    for i in st5_rev.keys():
        h = sq - i
        if h in st5_rev.keys() and h != i:
            vals = [st5_rev[h], st5_rev[i], c]
            vals.sort()
            if sum(vals) == 1000:
                vals = [str(val) for val in vals]
                print(' '.join(vals))