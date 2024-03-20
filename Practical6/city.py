city_UK=[0.56,0.62,0.04,9.7]
city_CHN=[0.58,8.4,29.9,22.2]
city_UK.sort()
city_CHN.sort(reverse=True)
print(city_UK)
print(city_CHN)
import matplotlib.pyplot as plt
plt.figure()
plt.boxplot(city_UK,vert=True)
plt.figure()
plt.boxplot(city_CHN,vert=True)
plt.show()