import matplotlib.pyplot as plt


data = [0]*4300 + [1]*6900 + [3]*4900 + [5]*2000 + [10]* 2100
plt.hist(data, bins=[0, 1, 3, 5, 10, 24], range=(0, 24), normed=True)
plt.xlim(0, 24)
plt.show()
