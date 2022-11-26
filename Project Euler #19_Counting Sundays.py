from datetime import date


def num_sundays_on_first_of_month(year1, year2):
    num_sundays = 0
    for i in range(year1, year2 ):
        for j in range(1, 13):
            if date(i, j, 1).weekday() == 6:
                num_sundays += 1
                print(date(i, j, 1))
    return num_sundays


T = 1
while T > 0:
    Y1, M1, D1 = 2000,1,1
    Y2, M2, D2 = 2020,1,1




    print(num_sundays_on_first_of_month(Y1, Y2))

    T -= 1

