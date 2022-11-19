# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
sums = 0
while N>0:
    sums += int(input())
    N -=1

print(str(sums)[:10])
