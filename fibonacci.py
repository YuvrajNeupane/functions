def gen_fib(n):
    first = 0
    second = 1
    print(first)
    print(second)

    for i in range(2,n):
        final = first + second
        first = second
        second = final
        print(final)
print(gen_fib(7))