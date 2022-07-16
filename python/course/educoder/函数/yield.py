def fib():
    a = 1
    b = 1
    yield a  # 第一次的返回值
    yield b  # 第二次的返回值
    while True:
        a, b = b, a + b
        yield b  # 后面项的返回值


s = 0
f = fib
n = 5
for i in range(n + 1):
    s += next(f)
print(s)
