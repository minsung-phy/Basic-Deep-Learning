# 1. 0~100까지 홀수의 합을 구하는 프로그램 작성
sum = 0

for x in range(0, 101):
    if x % 2 == 1:
        sum = sum + x

print(sum)