import time
def memo(fn):
    in_out_hash = {}

    def f(*args):
        if args in in_out_hash:
            return in_out_hash[args]

        in_out_hash[args] = fn(*args)
        return in_out_hash[args]

    return f

@memo
def fibonacci_mit_deko(n):
    if n < 2:
        return n
    return fibonacci_mit_deko(n-1) + fibonacci_mit_deko(n-2)



memo = [1,1]
def fibonacci_loop(n):
    global memo
    if len(memo) >= n:
        return memo[n]
    else:
        k = len(memo) - 1
        a, b = memo[-2], memo[-1]
    while k < n:
        memo.append(b)
        a, b = b, a + b
        k += 1
    return b




def prim(n):
    global memo
    # primzahl berechnung hier

start = time.time()
n = 5*10**5
print(f"deko({n})")
fibonacci_loop(n)
print(f"in {time.time()-start:.16f} sekunden")
start = time.time()
n = 55000
print(f"deko({n})")
prim(n)
print(f"in {time.time()-start:.16f} sekunden")
"""
start = time.time()
n = 490
x = 1
print(f"deko({n})x{x}")
for i in range(x):
    fibonacci_mit_deko(n)
print(f"in {time.time()-start:.16f} sekunden")

start = time.time()
n = 490
x = 1
print(f"loop({n})x{x}")
for i in range(x):
    fibonacci(n)
print(f"in {time.time()-start:.16f} sekunden")




#start = time.time()
#print("ohne:", fibonacci(30), f"in {time.time()-start:4f} sekunden")
"""





