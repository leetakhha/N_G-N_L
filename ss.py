import time


def sum_sq(n):
    s=0
    for x in range(1, n+1):
        s=s+x*x
    return s

def sum_sq1(n):
    s=0
    for x in range(1, n+1):
        s=s+x*x
    return s

start = time.time()
print(sum_sq(57575))
stop=time.time()

print("time : ", stop-start)

start1 = time.time()
print(sum_sq1(81312))
stop1=time.time()


print("time : ", stop1-start1)