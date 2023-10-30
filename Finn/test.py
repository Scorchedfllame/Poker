import time

start = time.perf_counter()
time.sleep(5)
end = time.perf_counter()
print(end - start)
time.sleep(1)
start1 = time.time()
time.sleep(5)
end1 = time.time()
print(end1 - start1)
