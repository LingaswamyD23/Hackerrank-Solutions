import math

for _ in range(int(input())):
    N,M = map(int, input().split())
    n_permutations = math.factorial(N + M) // (math.factorial(N) * math.factorial(M))
    solution = int(n_permutations % 1000000007)
    print(solution)
    print(math.factorial(N + M),  math.factorial(N), (math.factorial(N) * math.factorial(M)))