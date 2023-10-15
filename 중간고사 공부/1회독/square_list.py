# x 리스트에 n, y 리스트에 n*n을 넣는다
x = []
y = []

for n in range(10):
    print("The square of", n , "is", n*n)
    x.append(n)
    y.append(n*n)
    print(x[n])
    print(y[n])

print("done")