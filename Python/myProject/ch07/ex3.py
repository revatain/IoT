# ex3.py

# 1~100사이의 값들 중 짝수는 aa, 홀수는 bb

aa = []
bb = []

for i in range(0, 101, 1):
    if i % 2 == 0:
        aa.append(i)
    else:
        bb.append(i)
print("aa => ", aa)
print("bb => ", bb)