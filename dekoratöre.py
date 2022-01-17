

def dekorator(fn):
    def f(*args, **kwargs):
        print(f"prim mit {args[0]}")
        a =  fn(*args, **kwargs)
        print("funktion fertig")
        return a
    return f

@dekorator
def prim(n):
    if n<5:
        return [2,3,5]
    else:
        return []


print(prim(4))




def deko(fn):
    def f2(*args, **kwargs):
        print("erstes ergebnis")
        s = fn(*args, **kwargs)
        print("fertig")
        return s
    return f2

@deko
def rechnet(n, m):
    return n *100 / m *2

print(rechnet(20, 50))

