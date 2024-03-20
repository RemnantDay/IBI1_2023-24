dic={"sleep":8, "classes":6, "study":3.5, "TV":2, "music":1, "other":24-8-6-3.5-2-1}  # Create a dictionary for different activities
print(dic)  # Print the dictionary
values=list(dic.values()) # Get all the values in the dictionary
keys=list(dic.keys()) # Get all the keys in the dictionary
import matplotlib.pyplot as plt
plt.figure()
plt.pie(values,labels=keys,startangle=90,explode=[0,0,0.1,0,0,0])  # create the par chart, and the "study" part will be moved out a little bit
plt.show()
plt.clf()

###The following code is used to ask the user to input the activity they want to learn
activity=str(input("Input the activity you want to know (From 'sleep','classes','study','TV','music','other'):"))
print("You spent",dic[activity],"hours on",activity,"during an average day.")   # output the results
