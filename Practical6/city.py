city_UK=[0.56,0.62,0.04,9.7]
city_UK1=[0.56,0.62,0.04,9.7]  # make the same variable as city_UK for barplot (or it will be sorted and can't be the same as x labels created)
city_CHN=[0.58,8.4,29.9,22.2]
city_CHN1=[0.58,8.4,29.9,22.2]
city_UK.sort()  # sort values from smaller to bigger for cities in the UK
city_CHN.sort(reverse=True)  # sort values from bigger to smaller for cities in China
print(city_UK)
print(city_CHN)
x=[0,1,2,3]
x1=['Edinburgh','Glasgow','Stirling','London']  #Create x labels (city names in the UK)
x2=['Haining','Hangzhou','Shanghai','Beijing']  # Create y labels (city names in China)
color=['red','yellow','peru','deepskyblue']  # Create city types 
import matplotlib.pylab as plt
plt.figure()
plt.xticks(x, x1)  
plt.xlabel("city in the UK") # create x label name
plt.ylabel("population(millions)") # create y label name
plt.title("city size in the UK") # add a title to the figure
plt.bar(x1, city_UK1,color=color) # create the bar plot
plt.figure()
plt.xticks(x,x2)
plt.xlabel("city in China") # create x label name
plt.ylabel("population(millions)") # create y label name
plt.title("city size in China") # add a title to the figure
plt.bar(x2,city_CHN1,color=color)  # create the bar plot
plt.show()
plt.xticks(x,x2)
plt.xlabel("city in China")
plt.ylabel("population(millions)")
plt.title("city size in China")
plt.bar(x2,city_CHN1,color=color)
plt.show()
