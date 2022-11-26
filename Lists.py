if __name__ == '__main__':
    N = int(input())
    List = []
    for _ in range(N):
        comd = input()
        aist = comd.split(" ")
        if comd[0] == "i":
            List.insert(int(comd[7]),int(aist[-1]))
        elif comd[0] == "p" and comd[1] == "r" :
            print(List)
        elif comd[0] == "r" and comd[2] == "m":
            List.remove(int(aist[-1]))
        elif comd[0] == "a":
            List.append(int(aist[-1]))
        elif comd[0] == "s":
            List.sort()
        elif comd[0] == "p" and comd[1] == "o":
            List.pop(-1)
        else:
            List.reverse()