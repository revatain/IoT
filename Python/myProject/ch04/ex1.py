money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
money = int(input("교환할 돈은 얼마? "))
c500 = money//500
money %= 500
print(c500, ", ", money)