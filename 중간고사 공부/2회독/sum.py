# 1. 1 ~ 10까지 홀수들의 합을 구하시오.
# 2. 1 ~ 100까지 짝수들의 합을 구하시오.
# 3. 1 ~ 10000까지 7로 나누어 나머지가 2인 값들의 합을 구하시오.
# 4. 1 ~ 100까지 3으로 나누어 나머지가 2인 값들의 합을 구하시오.
# 5. 1 ~ 10000까지 7로 나누어 나머지가 2인 수 중 3으로 나누어 나머지가 0인 값들의 합을 구하시오.
# 6. 1 ~ 10000까지 7로 나누어 나머지가 2인 수 중 3으로 나누어 나머지가 0인 값 중 5로 나누어 나머지가 3인 값들의 합을 구하시오.

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0

for n in range(11):
    if n % 2 == 1:
        sum1 += n

print(sum1)

for n in range(101):
    if n % 2 == 0:
        sum2 += n

print(sum2)

for n in range(10001):
    if n % 7 == 2:
        sum3 += n

print(sum3)

for n in range(101):
    if n % 3 == 2:
        sum4 += n

print(sum4)

for n in range(10001):
    if n % 7 == 2:
        if n % 3 == 0:
            sum5 += n

print(sum5)

for n in range(10001):
    if n % 7 == 2:
        if n % 3 == 0:
            if n % 5 == 3:
                sum6 += n

print(sum6)