# Enter your code here. Read input from STDIN.
T = int(input())
while T>0:
   N = int(input())
   power = int(pow(2,N))
   sums = 0
   if power<10:
       print(power)
   else:
       while power>0:
           sums += power%10
           power //=10
       print(sums)
   T -=1