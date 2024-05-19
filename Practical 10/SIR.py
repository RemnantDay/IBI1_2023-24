# import necessary libraries       # ATTENTION: there is chance that the plot is 0 all the time. If that happens, please try it again and it will output correct results!
import numpy as np
import matplotlib .pyplot as plt
import random
N=10000            # Population Size
beta=0.3           # Beta
gamma=0.05         # Gamma
sus=list(range(1,9999+1))       # create a susceptible patients list, name each patient 1,2,3,...,9999
number_sus=[]
number_sus.append(9999)         # Create and calculate the number of susceptible patients, at first it's 9999
number_inf=[]
number_inf.append(1)            # Create and calculate the number of infected patients, at first it's 1
number_rec=[]
number_rec.append(0)            # Create and calculate the number of recovered patients, at first no body.
inf=[]
inf.append(10000)               # Assume the patient with number 10000 has infected the disease
rec=[]                          
time=list(range(1,1000+1))      # to help draw the plot later
for i in range (1,1000):
    aa=np.random.choice(range(2),len(sus),p=[beta*len(inf)/N,1-beta*len(inf)/N]) # Create a list with all 0(infected) and 1(still susceptible), with the same length of susceptible patients
    a=np.random.choice(range(2),len(inf),p=[gamma,1-gamma])  # Create a list with all 0(recovered) and 1 (still infected), with the same length of already infected patients
    b=len(inf)
    for j in range (0,len(sus)):      # ergodic each person in the susceptible list. (CASE 1)
        if aa[j]==0: # if the person is given the number 0, than he is infected
            inf.append(sus[j])      # Add the number of the person to the infected list
    for k in range (0,b): # ergodic each person in the infected list. (CASE 2)
        if a[k]==0:  # if the person is given the number 0, than he is recovered
            rec.append(inf[k])# Add the number of the person to the recovered list
    sus=[x for x in sus if x not in inf]# remove the infected person from susceptible list in CASE 1
    inf=[y for y in inf if y not in rec]# remove the recovered person from the infected list in CASE 2
    inf=[y for y in inf if y not in sus]# ensure no overlap in the infected and susceptible list
    number_sus.append(len(sus)) # get the number of susceptible people and add it to number_sus
    number_inf.append(len(inf))      # get the number of infected people and add it to number_inf
    number_rec.append(len(rec)) # get the number of recovered people and add it to number_rec
# print(number_sus)
# print(number_inf)
# print(number_rec)

data_dict1={}
data_dict2={}
data_dict3={}
for i,j in zip(time,number_sus):           
    data_dict1[i]=j
for i,j in zip(time,number_inf):
    data_dict2[i]=j
for i,j in zip(time,number_rec):
    data_dict3[i]=j    
plt.title("SIR model")
plt.xlabel("time")
plt.ylabel('number of people')
x=[i for i in data_dict1.keys()]        # set x axis (time), that is, keys in the dictionary
y1=[i for i in data_dict1.values()]  # set y axis (susceptible people),that is, values in data_dict1
y2=[i for i in data_dict2.values()] # set y axis (infected people),that is, values in data_dict2
y3=[i for i in data_dict3.values()]  # set y axis (recovered people),that is, values in data_dict3
plt.plot(x,y1,label="suspectible")
plt.plot(x,y2,label="infected")
plt.plot(x,y3,label="recovered")
plt.legend()
plt.show()
