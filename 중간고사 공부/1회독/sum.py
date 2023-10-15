# 1. 0~10까지 2로 나누어서 나머지가 1인 값들(홀수)의 합
sum1 = 0

for x in range(11):
    if (x % 2 == 1):
        sum1 = sum1 + x

print(sum1)

# 2. 0~100까지 2로 나누어서 나머지가 0인 값들(짝수)의 합
sum2 = 0

for x in range(101):
    if (x % 2 == 0):
        sum2 = sum2 + x

print(sum2)

# 3. 0~100까지 3으로 나누어서 나머지가 2인 값들의 합
sum3 = 0

for x in range(101):
    if x % 3 == 2:
        sum3 = sum3 + x

print(sum3)

# 4. 0~10000까지 7로 나누어서 나머지가 2인 값들의 합
sum4 = 0

for x in range(10001):
    if x % 7 == 2:
        sum4 = sum4 + x

print(sum4)

# 5. 0~10000까지 7로 나누어서 나머지가 2인 값 중 3으로 나누어서 나머지 0인 값들의 합
sum5 = 0

for x in range(10001):
    if x % 7 == 2:
        if x % 3 == 0:
            sum5 = sum5 + x

print(sum5)

# 6. 0~10000까지 7로 나누어서 나머지가 2인 값 중 3으로 나누어서 나머지가 0인 값 중 5로 나누어서 나머지가 3인 값들의 합
sum6 = 0

for x in range(10001):
    if x % 7 == 2:
        if x % 3 == 0:
            if x % 5 == 3:
                sum6 = sum6 + x

print(sum6)