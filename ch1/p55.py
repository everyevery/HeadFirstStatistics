import matplotlib.pyplot as plt
import numpy as np


areas = ['북아메리카', '남아메리카', '유럽', '아시아', '오세아니아', '아프리카', '남극']
data = [1500, 500, 1500, 2000, 1000, 500, 1]


plt.bar(np.arange(0.7, len(areas), 1), data, width=0.6)
plt.xticks(np.arange(1, len(areas)+1, 1), areas)
plt.ylim(0, 2500)
plt.show()
