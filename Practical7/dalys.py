import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("E:/IBI1/IBI1_2023-24/Practical7")
#print(os.getcwd())
#print(os.listdir())
dalys_data=pd.read_csv("E:/IBI1/IBI1_2023-24/Practical7/dalys-rate-from-all-causes.csv")
#print(dalys_data.head(5))
#print(dalys_data.info())
#print(dalys_data.describe())
#print(dalys_data.iloc[0,3])
#print(dalys_data.iloc[2,0:5])
#print(dalys_data.iloc[0:2,:])
#print(dalys_data.iloc[0:10:2,0:5])
print(dalys_data.iloc[0:101:10,3])          #ATTENTION: This line tries to show the fourth column from every 10th row, starting from the first row, for the first 100 rows(inclusive)
#print(dalys_data.loc[2:4,"Year"])
dalys_data1=dalys_data[dalys_data["Entity"]=="Afghanistan"]  #ATTENTION: This line tries to select "Afghanistan" rows in "Entity" only by using Boolean "=="
print(dalys_data1.loc[:,"DALYs"])     
china_data=dalys_data[dalys_data["Entity"]=="China"]
print(np.mean(china_data.loc[:,"DALYs"]))  #ATTENTION: This line shows the mean DALYs in China over time (30677)
china_data_2019=china_data[china_data["Year"]==2019]  
print(np.mean(china_data_2019.loc[:,"DALYs"]))  #ATTENTION: This line shows the mean DALYs in China in 2019 (22270)
# ! From the result of line 22 and line 23, I can see 2019 is below the mean.
plt.plot(china_data.Year, china_data.DALYs, "b+")  #The data points shown in the plot have the shape "+"
plt.xticks(china_data.Year,rotation=-90)       #This line rotates the x labels 90 degrees clockwise
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('The DALYs in China')
#plt.plot(china_data.Year, china_data.DALYs, "r+")
#plt.plot(china_data.Year, china_data.DALYs, "bo")
plt.show()

################################# My Another Question ############# My Another Question ##############################################
UK_data=dalys_data[dalys_data["Code"]=="GBR"]
plt.plot(china_data.Year,china_data.DALYs,label="China")
plt.plot(china_data.Year,UK_data.DALYs,color="red",linewidth=1,linestyle='--',label="UK")
plt.legend()
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('The DALYs in China and the UK over the years')
plt.show()
# ! From the plot we can see that the relationship between the DALYs in China and the UK are more similar.
