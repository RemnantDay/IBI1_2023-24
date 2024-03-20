city_UK=[0.56,0.62,0.04,9.7]
city_CHN=[0.58,8.4,29.9,22.2]
city_UK.sort()  # sort values from smaller to bigger
city_CHN.sort(reverse=True)  # sort values from bigger to smaller
print(city_UK)
print(city_CHN)
import matplotlib.pyplot as plt
plt.figure()
plt.boxplot(city_UK,vert=True,showmeans=True,widths=0.1)
plt.suptitle("The Boxplot of population in the UK",fontsize=15) #设置字体大小为15号字体
plt.figure()
plt.boxplot(city_CHN,vert=False,showmeans=True)
plt.suptitle("The Boxplot of population in China",fontsize=15)
plt.show()