import numpy as np

def net(w1, i1, w2, i2, b):
    return w1 * i1 + w2 * i2 + b

def output(net):
    return 1/(1+np.exp(-net))

neth1 = net(0.15, 0.05, 0.20, 0.10, 0.35)
print(neth1)
print(output(neth1))

neth2 = net(0.25, 0.05, 0.30, 0.10, 0.35)
print(neth2)
print(output(neth2))

neto1 = net(0.40, output(neth1), 0.45, output(neth2), 0.60)
print(neto1)
print(output(neto1))

neto2 = net(0.55, output(neth2), 0.50, output(neth1), 0.60)
print(neto2)
print(output(neto2))






