sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0

for n in range(11):
    if n % 2 == 1:
        sum1 = sum1 + n
print(sum1)

for n in range(101):
    if n % 2 == 0:
        sum2 = sum2 + n
print(sum2)

for n in range(101):
    if n % 3 == 2:
        sum3 = sum3 + n
print(sum3)

for n in range(10001):
    if n % 7 == 2:
        sum4 = sum4 + n
print(sum4)

for n in range(10001):
    if n % 7 == 2:
        if n % 3 == 0:
            sum5 = sum5 + n
print(sum5)

for n in range(10001):
    if n % 7 == 2:
        if n % 3 == 0:
            if n % 5 == 3:
                sum6 = sum6 + n
print(sum6)
