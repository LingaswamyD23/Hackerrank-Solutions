def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        subsequence = ""
        substring = string[i:(i + k)]
        for l in substring:
            if l not in subsequence:
                subsequence += l
        print(subsequence)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)