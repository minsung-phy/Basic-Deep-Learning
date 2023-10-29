# 100보다 작은 자연수들 중 3의 배수이면서 2의 배수이면서 5로 나누어서 나머지가 1인 수들의 합을 구하시오.

sum = 0

for x in range(100):
    if x % 3 == 0:
        if x % 2 == 0:
            if x % 5 == 1:
                sum += x

print(sum)
