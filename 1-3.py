import time

def sum_sq(n):
    return n*(n+1)*(2*n*1)//6

def sum_sq123(n):
    return n*(n+1)*(2*n*1)//6

start = time.time()

print(sum_sq(2221))

stop = time.time()

start12 = time.time()

print(sum_sq123(222231))

stop12 = time.time()

print("time : ", stop-start)
print("time : ", stop12-start12)