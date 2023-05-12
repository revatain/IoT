#ex2.py

i, sum = 0, 0
num1, num2 , num3 = 0, 0, 0

num1 = int(input("시작값을 입력하세요 : "))
num2 = int(input("마지막값을 입력하세요 : "))
num3 = int(input("증가값을 입력하세요 : "))

for i in range(num1, num2+1, num3):
    sum += i
print("%d에서 %d까지 %d씩 증가시킨 합계 : %d" %(num1, num2, num3, sum))

#i가 필요없을때 '_' 사용
for _ in range(1, 5):
    print("반갑습니다")






