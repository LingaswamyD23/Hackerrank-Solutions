#
# __problem__ = """
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# """
#
# # ---------------------------------------------------------
#
#
# # # 1 # this solution is just the solution to the problem on the https://projecteuler.net/problem=9:
# # and this solitions is too slow
# def pythagor(N):
#     num = list(range(1, int(N//2)))
#     for a in num:
#         for b in num:
#             if pow(a, 2) + pow(b, 2) == pow(N - a - b, 2): return (a * b * (N - a - b))
# # print(pythagor(1000))
#
#
# def pythagorTri(N: int) -> int:
#     mx = -1
#     if N % 2 != 1:
#         # N must be even because:
#         """
#         a² + b² = c²,   a + b + c = N
#         O  + O  = E ,   O + O + E = E
#         O  + E  = O ,   O + E + O = E
#         E  + E  = E ,   E + E + E = E
#         """
#         # if N is an odd, print -1
#         for a in range(1, N // 3):
#             if (N ** 2 - (2 * (N) * (a))) % (2 * (N - a)) == 0:
#                 """
#                 N  =  a + b + c
#                 N² = (a + b + c)² = a² + b² + c² + 2(ab + ac + bc)
#
#                 a² + b² = c²
#
#                 N² = 2c² + 2(a(b + c) + bc)
#                 ===> 2(c² + a(b + c) + bc)
#
#                 N - a = b + c
#
#                 ===> 2(c² + a(N - a) + bc)
#                 ===> 2(c² + Na - a² + bc)
#
#                 b² = c² - a²
#
#                 N² - 2Na = 2(c² - a² + bc)
#
#                 N² - 2Na = 2(b² + bc)
#
#                     2(b(b + c))
#                 ==> -----------  =  b
#                       2(b + c)
#                 """
#                 b = N * (N - 2 * a) // (2 * (N - a))
#                 mx = max(mx, a * b * (N - a - b))
#     return mx
#
#
# for _ in range(int(input())):
#     print(pythagorTri(int(input())))
#
#
#

import sys

def isTriplet(n):
    m = -1
    if n%2 != 1:
        for a in range(1, n//3):
            if n*(n - 2*a)%(2*(n - a)) == 0:
                b = n*(n - 2*a)//(2*(n - a))
                m = max(m, a*b*(n - a - b))
    print(m)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    isTriplet(n)