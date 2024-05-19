# import necessary libraries  # ATTENTION: there is chance that the plot is 0 all the time. If that happens, please try it again and it will output correct results!
import numpy as np
import numpy as np
import matplotlib .pyplot as plt
import random
N=10000            # Population Size
beta=0.3           # Beta number
gamma=0.05         # Gamma number
sus=list(range(1,10000))    # Create a list of susceptible patients and number each patients from 1 to 10000 (no one get vaccinated)
sus1=list(range(1,9000))    # 10% people get vaccinated
sus2=list(range(1,8000))    # 20% people get vaccinated
sus3=list(range(1,7000))    # 30% people get vaccinated
sus4=list(range(1,6000))    # 40% people get vaccinated
sus5=list(range(1,5000))    # 50% people get vaccinated 
sus6=list(range(1,4000))    # 60% people get vaccinated
sus7=list(range(1,3000))    # 70% people get vaccinated
sus8=list(range(1,2000))    # 80% people get vaccinated
sus9=list(range(1,1000))    # 90% people get vaccinated
number_inf=[]               # Codes from this line to line 37 are used to calculate how many people are infected
number_inf.append(1)
number_inf1=[]
number_inf1.append(1)
number_inf2=[]
number_inf2.append(1)
number_inf3=[]
number_inf3.append(1)
number_inf4=[]
number_inf4.append(1)
number_inf5=[]
number_inf5.append(1)
number_inf6=[]
number_inf6.append(1)
number_inf7=[]
number_inf7.append(1)
number_inf8=[]
number_inf8.append(1)
number_inf9=[]
number_inf9.append(1)
inf=[]                    
inf.append(10000)      # Create a list of infected people. Assume that the person with number 10000 is infected at the beginning
inf1=[]
inf1.append(9000)   # Create a list of infected people. Assume that the person with number 9000 is infected at the beginning
inf2=[]
inf2.append(8000)
inf3=[]
inf3.append(7000)
inf4=[]
inf4.append(6000)
inf5=[]
inf5.append(5000)
inf6=[]
inf6.append(4000)
inf7=[]
inf7.append(3000)
inf8=[]
inf8.append(2000)
inf9=[]
inf9.append(1000)
rec=[]             # Create a list of recovered people. No one is recovered at the beginning so it is an empty list
rec1=[]
rec2=[]
rec3=[]
rec4=[]
rec5=[]
rec6=[]
rec7=[]
rec8=[]
rec9=[]
time=list(range(1,1000+1))         # create a list with times
for i in range (1,1000):           # Run the code for 1000 times
    aa=np.random.choice(range(2),len(sus),p=[beta*len(inf)/N,1-beta*len(inf)/N])     # certain amount of people get infected in each time, 0 (infected) and 1 (still susceptible)
    a=np.random.choice(range(2),len(inf),p=[gamma,1-gamma])     # certain amount of people get recovered, 0 (recovered) and 1 (Still infected)
    b=len(inf)
    for j in range (0,len(sus)):       # Traversal each person in the susceptible list. (CASE 1)
        if aa[j]==0:                  # if the person is given the number 0, than he is infected
            inf.append(sus[j])        # Add the number of the person to the infected list
    for k in range (0,b):               # Traversal each person in the infected list. (CASE 2)
        if a[k]==0:                        # if the person is given the number 0, than he is recovered
            rec.append(inf[k])          # Add the number of the person to the recovered list
    sus=[x for x in sus if x not in inf]  # remove the infected person from susceptible list in CASE 1
    inf=[y for y in inf if y not in rec]  # remove the recovered person from the infected list in CASE 2
    inf=[y for y in inf if y not in sus]  # ensure no overlap in the infected and susceptible list
    number_inf.append(len(inf))            # get the number of infected people and add it to another list to save it

for i in range (1,1000):                 # almost the same as the codes from line 69 to line 82. Only change the variables.
    a1=np.random.choice(range(2),len(sus1),p=[beta*len(inf1)/N,1-beta*len(inf1)/N])
    a2=np.random.choice(range(2),len(inf1),p=[gamma,1-gamma])
    b=len(inf1)
    for j in range (0,len(sus1)):
        if a1[j]==0:
            inf1.append(sus1[j])
    for k in range (0,b):
        if a2[k]==0:
            rec1.append(inf1[k])
    sus1=[x for x in sus1 if x not in inf1]
    inf1=[y for y in inf1 if y not in sus1]
    inf1=[z for z in inf1 if z not in rec1]
    number_inf1.append(len(inf1))

for i in range (1,1000):             # almost the same as the codes from line 69 to line 82. Only change the variables.
    a3=np.random.choice(range(2),len(sus2),p=[beta*len(inf2)/N,1-beta*len(inf2)/N])
    a4=np.random.choice(range(2),len(inf2),p=[gamma,1-gamma])
    b=len(inf2)
    for j in range (0,len(sus2)):
        if a3[j]==0:
            inf2.append(sus2[j])
    for k in range (0,b):
        if a4[k]==0:
            rec2.append(inf2[k])
    sus2=[x for x in sus2 if x not in inf2]
    inf2=[y for y in inf2 if y not in sus2]
    inf2=[z for z in inf2 if z not in rec2]
    number_inf2.append(len(inf2))

for i in range (1,1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a5=np.random.choice(range(2),len(sus3),p=[beta*len(inf3)/N,1-beta*len(inf3)/N])
    a6=np.random.choice(range(2),len(inf3),p=[gamma,1-gamma])
    b=len(inf3)
    for j in range (0,len(sus3)):
        if a5[j]==0:
            inf3.append(sus3[j])
    for k in range (0,b):
        if a6[k]==0:
            rec3.append(inf3[k])
    sus3=[x for x in sus3 if x not in inf3]
    inf3=[y for y in inf3 if y not in sus3]
    inf3=[z for z in inf3 if z not in rec3]
    number_inf3.append(len(inf3))

for i in range (1,1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a5=np.random.choice(range(2),len(sus3),p=[beta*len(inf3)/N,1-beta*len(inf3)/N])
    a6=np.random.choice(range(2),len(inf3),p=[gamma,1-gamma])
    b=len(inf3)
    for j in range (0,len(sus3)):
        if a5[j]==0:
            inf3.append(sus3[j])
    for k in range (0,b):
        if a6[k]==0:
            rec3.append(inf3[k])
    sus3=[x for x in sus3 if x not in inf3]
    inf3=[y for y in inf3 if y not in sus3]
    inf3=[z for z in inf3 if z not in rec3]
    number_inf3.append(len(inf3))

for i in range(1, 1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a7 = np.random.choice(range(2), len(sus4), p=[beta * len(inf4) / N, 1 - beta * len(inf4) / N])
    a8 = np.random.choice(range(2), len(inf4), p=[gamma, 1 - gamma])
    b = len(inf4)
    for j in range(0, len(sus4)):
        if a7[j] == 0:
            inf4.append(sus4[j])
    for k in range(0, b):
        if a8[k] == 0:
            rec4.append(inf4[k])
    sus4 = [x for x in sus4 if x not in inf4]
    inf4 = [y for y in inf4 if y not in sus4]
    inf4 = [z for z in inf4 if z not in rec4]
    number_inf4.append(len(inf4))

for i in range(1, 1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a9 = np.random.choice(range(2), len(sus5), p=[beta * len(inf5) / N, 1 - beta * len(inf5) / N])
    a10 = np.random.choice(range(2), len(inf5), p=[gamma, 1 - gamma])
    b = len(inf5)
    for j in range(0, len(sus5)):
        if a9[j] == 0:
            inf5.append(sus5[j])
    for k in range(0, b):
        if a10[k] == 0:
            rec5.append(inf5[k])
    sus5 = [x for x in sus5 if x not in inf5]
    inf5 = [y for y in inf5 if y not in sus5]
    inf5 = [z for z in inf5 if z not in rec5]
    number_inf5.append(len(inf5))

for i in range(1, 1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a11 = np.random.choice(range(2), len(sus6), p=[beta * len(inf6) / N, 1 - beta * len(inf6) / N])
    a12 = np.random.choice(range(2), len(inf6), p=[gamma, 1 - gamma])
    b = len(inf6)
    for j in range(0, len(sus6)):
        if a11[j] == 0:
            inf6.append(sus6[j])
    for k in range(0, b):
        if a12[k] == 0:
            rec6.append(inf6[k])
    sus6 = [x for x in sus6 if x not in inf6]
    inf6 = [y for y in inf6 if y not in sus6]
    inf6 = [z for z in inf6 if z not in rec6]
    number_inf6.append(len(inf6))

for i in range(1, 1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a13 = np.random.choice(range(2), len(sus7), p=[beta * len(inf7) / N, 1 - beta * len(inf7) / N])
    a14 = np.random.choice(range(2), len(inf7), p=[gamma, 1 - gamma])
    b = len(inf7)
    for j in range(0, len(sus7)):
        if a13[j] == 0:
            inf7.append(sus7[j])
    for k in range(0, b):
        if a14[k] == 0:
            rec7.append(inf7[k])
    sus7 = [x for x in sus7 if x not in inf7]
    inf7 = [y for y in inf7 if y not in sus7]
    inf7 = [z for z in inf7 if z not in rec7]
    number_inf7.append(len(inf7))

for i in range(1, 1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a15 = np.random.choice(range(2), len(sus8), p=[beta * len(inf8) / N, 1 - beta * len(inf8) / N])
    a16 = np.random.choice(range(2), len(inf8), p=[gamma, 1 - gamma])
    b = len(inf8)
    for j in range(0, len(sus8)):
        if a15[j] == 0:
            inf8.append(sus8[j])
    for k in range(0, b):
        if a16[k] == 0:
            rec8.append(inf8[k])
    sus8 = [x for x in sus8 if x not in inf8]
    inf8 = [y for y in inf8 if y not in sus8]
    inf8 = [z for z in inf8 if z not in rec8]
    number_inf8.append(len(inf8))

for i in range(1, 1000): # almost the same as the codes from line 69 to line 82. Only change the variables.
    a17 = np.random.choice(range(2), len(sus9), p=[beta * len(inf9) / N, 1 - beta * len(inf9) / N])
    a18 = np.random.choice(range(2), len(inf9), p=[gamma, 1 - gamma])
    b = len(inf9)
    for j in range(0, len(sus9)):
        if a17[j] == 0:
            inf9.append(sus9[j])
    for k in range(0, b):
        if a18[k] == 0:
            rec9.append(inf9[k])
    sus9 = [x for x in sus9 if x not in inf9]
    inf9 = [y for y in inf9 if y not in sus9]
    inf9 = [z for z in inf9 if z not in rec9]
    number_inf9.append(len(inf9))


data_dict={}        # Create an empty dictionary for each case
data_dict1={}
data_dict2={}
data_dict3={}
data_dict4={}
data_dict5={}
data_dict6={}
data_dict7={}
data_dict8={}
data_dict9={}
data_dict10={}
t10=[0]*1000
for i,j in zip(time,number_inf):         # Add time as x axis, number of infected people as y axis to the dictionary
    data_dict[i]=j  
for i,j in zip(time,number_inf1):
    data_dict1[i]=j 
for i,j in zip(time,number_inf2):
    data_dict2[i]=j   
for i,j in zip(time,number_inf3):
    data_dict3[i]=j   
for i,j in zip(time,number_inf4):
    data_dict4[i]=j     
for i,j in zip(time,number_inf5):
    data_dict5[i]=j    
for i,j in zip(time,number_inf6):
    data_dict6[i]=j
for i,j in zip(time,number_inf7):
    data_dict7[i]=j
for i,j in zip(time,number_inf8):
    data_dict8[i]=j
for i,j in zip(time,number_inf9):
    data_dict9[i]=j
for i,j in zip(time,t10):
    data_dict10[i]=j
plt.title("SIR model with different vaccination rates")
plt.xlabel("time")
plt.ylabel('number of people')
x=[i for i in data_dict.keys()]           # set x axis (time), that is, keys in the dictionary
y=[i for i in data_dict.values()]         # set y axis (infected people),that is, values in the dictionary
y1=[i for i in data_dict1.values()]
y2=[i for i in data_dict2.values()]
y3=[i for i in data_dict3.values()]
y4=[i for i in data_dict4.values()]
y5=[i for i in data_dict5.values()]
y6=[i for i in data_dict6.values()]
y7=[i for i in data_dict7.values()]
y8=[i for i in data_dict8.values()]
y9=[i for i in data_dict9.values()]
y10=[i for i in data_dict10.values()]
plt.plot(x,y,label="0")                 #label the plots
plt.plot(x,y1,label="10%")
plt.plot(x,y2,label="20%")
plt.plot(x,y3,label="30%")
plt.plot(x,y4,label="40%")
plt.plot(x,y5,label="50%")
plt.plot(x,y6,label="60%")
plt.plot(x,y7,label="70%")
plt.plot(x,y8,label="80%")
plt.plot(x,y9,label="90%")
plt.plot(x,y10,label="100%")
plt.legend()
plt.show()
