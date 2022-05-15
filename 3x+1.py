import matplotlib.pyplot as plt
import numpy as np

x = int(input())
y = []

y.append(x)

while x>1:
    if x%2==0:
        x = x/2
    else:
        x = 3*x+1
    y.append(x)


xaxis = np.arange(0, len(y))
y = np.array(y)

plt.plot(xaxis,y)
plt.show()