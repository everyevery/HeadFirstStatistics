from matplotlib import pyplot as plt

fig, axes = plt.subplots(ncols=2)

axes[0].set_xlim(18, 23)
axes[0].set_ylim(0, 5)
axes[0].bar((19, 20, 21), (1, 3, 1), width=1)

axes[1].set_xlim(18, 150)
axes[1].set_ylim(0, 10)
axes[1].bar((19, 20, 21, 145, 147), (3, 6, 3, 1, 1), width=1)

plt.show()
