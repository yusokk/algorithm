this_year = int(input())

def yun_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(1)
    elif year % 400 == 0:
        print(1)
    else:
        print(0)

yun_year(this_year)