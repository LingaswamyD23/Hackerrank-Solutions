if __name__ == '__main__':
    student_ = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_.append([name, score])
        scores.append(score)

    s_set = sorted(set(scores), reverse=False)

    names = []
    for v in student_:
        if v[1] == s_set[1]:
            names.append(v[0])

    names.sort()
    for name in names:
        print(name)


