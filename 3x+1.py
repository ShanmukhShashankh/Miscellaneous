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

max = int(y.max())
index = np.where(y==max)
xmax = int(xaxis[index])

end = int(y.min())
end_index = np.where(y==end)
xmin = int(xaxis[end_index])


plt.plot(xaxis,y)
plt.annotate(f'({int(xaxis[0])}, {int(y[0])})', xy=(int(xaxis[0]), int(y[0])))
plt.annotate(f'({xmax}, {max})', xy=(xmax, max))
plt.annotate(f'({xmin}, {end})', xy=(xmin, end))
plt.show()

