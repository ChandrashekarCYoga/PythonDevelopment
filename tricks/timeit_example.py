# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit


print(timeit.timeit('"_".join(str(n) for n in range(100))', number=10000))


print(timeit.timeit('"_".join([str(n) for n in range(100)])', number=10000))


print(timeit.timeit('"_".join(map(str, range(100)))', number=10000))
