def palindromisch(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False


"""for i in range(10, 10001):
    count = 0
    if str(i)[-1] == "0":
        continue
    i = i + int(str(i)[::-1]):
    count += 1
        if palindromisch(i):
            break
        else:"""

def lychel(n, wh = 0):
    add = n + int(str(n)[::-1])
    #print(add)
    if palindromisch(add):
        return False

    if wh == 50:
        return True
    return lychel(add, wh + 1)

count = 0
for i in range(10, 10001):
    if lychel(i):
        count += 1
print(count)



