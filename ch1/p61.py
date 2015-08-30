import matplotlib.pyplot as plt

data = [100, 100, 100, 100, 100, 300, 300, 300, 300, 500, 500, 500, 500, 500, 500, 600, 600, 800]
plt.hist(data, 5, range=(0, 1000))
plt.ylim(10)
plt.ylim(0, 10)
plt.show()
