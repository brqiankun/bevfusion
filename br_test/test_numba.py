from numba import jit
import numpy as np
import time

x = np.arange(100).reshape(10, 10)

@jit(nopython=True)
def go_fast(a):
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

start = time.perf_counter()
go_fast(x)
end = time.perf_counter()
print("elapsed (with compilation) = {}s".format((end - start)))

start = time.perf_counter()
go_fast(x)
end = time.perf_counter()
print("elapsed (after compilation) = {}s".format((end - start)))