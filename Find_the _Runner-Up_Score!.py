if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a_set = set(arr)
    a_set = sorted(a_set, reverse = True)
    print(a_set[1])