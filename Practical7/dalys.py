import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np                  # import necessary libraries
os.chdir("E:/IBI1/IBI1_2023-24/Practical7")
#print(os.getcwd())
#print(os.listdir())
dalys_data=pd.read_csv("E:/IBI1/IBI1_2023-24/Practical7/dalys-rate-from-all-causes.csv")      # import the csv file

print(dalys_data.iloc[0:101:10,3])          #ATTENTION:This line tries to show the fourth column from every 10th row, starting from the first row, for the first 100 rows(inclusive)
Afg = []
for i in range(0,dalys_data.shape[0]):
    if dalys_data.iloc[i,0] == 'Afghanistan':
        Afg.append(True)
    else:
        Afg.append(False)  #ATTENTION: These lines select "Afghanistan" rows in "Entity" by using Boolean
print(dalys_data.loc[Afg,"DALYs"])    
China = []
for i in range(0,dalys_data.shape[0]):
    if dalys_data.iloc[i,0] == 'China':
        China.append(True)
    else:
        China.append(False)     #ATTENTION: These lines select "China" rows in "Entity" by using Boolean (similar)
china_data = dalys_data.iloc[China, :]

print('The mean DALYs in China:',np.mean(dalys_data.loc[China,"DALYs"]))  #ATTENTION: This line shows the mean DALYs in China over time (30677)
china_data_2019=china_data[china_data["Year"]==2019]  
print("The mean DALYs in China in 2019 (attention: in 2019!):",np.mean(china_data_2019.loc[:,"DALYs"]))  #ATTENTION: This line shows the mean DALYs in China in 2019 (22270)
# ! From the result, I can see the DALYs in China in 2019 was less than the mean.
print("The DALYs in China in 2019 was less than the mean.")
plt.plot(china_data.Year, china_data.DALYs, "b+")  #The data points shown in the plot have the shape "+"
plt.xticks(china_data.Year,rotation=-90)       #This line rotates the x labels 90 degrees clockwise
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('The DALYs in China') # Add a title to the plot
plt.show()

################################# My Another Question #######################################
# My question is: How has the relationship between the DALYs in China and the UK changed over time, more similar or less similar?
UK_data=dalys_data[dalys_data["Code"]=="GBR"]
plt.plot(china_data.Year,china_data.DALYs,label="China")    # Create a line about DALYs in China
plt.plot(china_data.Year,UK_data.DALYs,color="red",linewidth=1,linestyle='--',label="UK")    # Create a different line about DALYs in the UK
plt.legend()
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('The DALYs in China and the UK over the years') # Add a title to the plot
plt.show()
# ! From the plot we can see that the relationship between the DALYs in China and the UK are more similar.
print("The results for my another question: From the plot we can see that the relationship between the DALYs in China and the UK are more similar")
