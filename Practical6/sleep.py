dic={"sleep":8, "classes":6, "study":3.5, "TV":2, "music":1, "other":24-8-6-3.5-2-1}
print(dic)
values=list(dic.values())
keys=list(dic.keys())
import matplotlib.pyplot as plt
plt.figure()
plt.pie(values,labels=keys,startangle=90,explode=[0,0,0.1,0,0,0])
plt.show()
plt.clf()

###The following code is used to ask the user to input the activity they want to learn
activity=str(input("Input the activity you want to know (sleep,classes,study,TV,music,other):"))
print("You spent",dic[activity],"hours on",activity,"in average.")   # output the result