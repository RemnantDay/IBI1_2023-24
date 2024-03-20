dic={"sleep":8, "classes":6, "study":3.5, "TV":2, "music":1, "other":24-8-6-3.5-2-1}
print(dic)
values=list(dic.values())
keys=list(dic.keys())
import matplotlib.pyplot as plt
plt.figure()
plt.pie(values,labels=keys,startangle=90,explode=[0,0,0.1,0,0,0])
plt.show()
plt.clf()

###The following code is used to ask the user to input their own time and print out their own dictionary
sleep=float((input("Your own Sleep hours:")))
classes=float(input("Your own Classes hours:"))
study=float(input("Your own Study hours:"))
TV=float(input("Your own TV hours:"))
music=float(input("Your own Music hours:"))
newdic={"Sleep":sleep, "Classes":classes, "Study":study, "TVs":TV, "Music":music, "Other":24-sleep-classes-study-TV-music}
print(newdic)
activity=str(input("Input the activity you want to know (Sleep,Classes,Study,TVs,Music,Other):"))
print("You spent",newdic[activity],"hours on",activity,"in average.")