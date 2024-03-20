city_UK=[0.56,0.62,0.04,9.7]
city_UK1=[0.56,0.62,0.04,9.7]
city_CHN=[0.58,8.4,29.9,22.2]
city_CHN1=[0.58,8.4,29.9,22.2]
city_UK.sort()  # sort values from smaller to bigger
city_CHN.sort(reverse=True)  # sort values from bigger to smaller
print(city_UK)
print(city_CHN)
x=[0,1,2,3]
x1=['Edinburgh','Glasgow','Stirling','London']
x2=['Haining','Hangzhou','Shanghai','Beijing']  
color=['red','yellow','peru','deepskyblue']
import matplotlib.pylab as plt
plt.figure()
plt.xticks(x, x1)  
plt.xlabel("city in the UK")
plt.ylabel("population(millions)")
plt.title("city size in the UK")
plt.bar(x1, city_UK1,color=color)
plt.figure()
plt.xticks(x,x2)
plt.xlabel("city in China")
plt.ylabel("population(millions)")
plt.title("city size in China")
plt.bar(x2,city_CHN1,color=color)
plt.show()