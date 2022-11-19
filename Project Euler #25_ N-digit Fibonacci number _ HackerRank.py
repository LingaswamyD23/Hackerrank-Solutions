# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import log10,sqrt

def n_fibo(n):
    if n == 1:
        return 1
    phi_log = log10((1 + sqrt(5))/2)
    log_10 = ((log10(5)) / 2)
    return(int((n+log_10-1)/phi_log) + 1)

for _ in range(int(input())):
    print(n_fibo(int(input())))
