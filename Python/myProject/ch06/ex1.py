#ex1.py

for i in range(0, 3):
    print("안녕하세요", i)

for i in range(0, 10 ,2):
    print("반갑습니다", i)

sum = 0
for i in range (1, 11):
    sum += i
print("sum : ", sum)

## 500과 1000사이의 홀수의 합계
sum = 0
for i in range(500, 1001):
    if(i%2==0):
        sum += i
print("sum : ", sum)

sum = 0
for i in range(500, 1001, 2):
        sum += i
print("sum : ", sum)

