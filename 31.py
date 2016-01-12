import time
start_time = time.time()

def make_change(amt, denom):
    denom.sort(reverse=True)
    if amt == 0:
        return 1
    if denom[0] == 1:
        return 1
    index = 0
    while amt / denom[index] < 1:
        index += 1
    if denom[index] == 1:
        return 1
    return make_change(amt - denom[index], denom[index:]) + make_change(amt, denom[(index + 1):])

print(make_change(200, [200, 100, 50, 20, 10, 5, 2, 1]))
print("%s seconds" % (time.time() - start_time))