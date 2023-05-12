# ex6.py

select, answer, numStr , num1, num2 = 0, 0, "", 0, 0

select = int(input("1.입력한 수식 계산 2.두 수 사이의 합계 : "))

if select == 1:
    numStr = input("***수식을 입력하세요 : ")
    answer = eval(numStr)
    print("%s 결과는 %5.1f입니다 " %(numStr, answer))
elif select == 2:
    num1 = int(input("***첫번째 숫자를 입력 : "))
    num2 = int(input("***두번째 숫자를 입력 : "))
    ## for 출력 -> 1과 10는 사이의 합계는 55입니다.
    for i in range(num1, num2+1, 1):
        answer += i
    print("%d과 %d 사이의 합계는 %d" %(num1, num2, answer))
else:
    print("1또는 2만 입력을 해야 합니다")