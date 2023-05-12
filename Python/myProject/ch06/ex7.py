# ex7.py

sum, a, b = 0, 0, 0

while True:
    a = int(input("더 할 첫번째 수를 입력하세요 : "))
    if a == 0:
        break
    b = int(input("더 할 두번째 수를 입력하세요 : "))
    sum = a + b
    print("%d + %d = %d" % (a, b, sum))

print("0을 입력해 반복문을 빠져 나온다")

sum = 0
for i in range(1, 101):
    if i % 3 == 0:
        continue
    sum += i

print("1~100의 합계(3의 배수는 제외) : %d" % sum)





