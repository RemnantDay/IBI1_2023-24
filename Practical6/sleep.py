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
sleep=float((input("Sleep hours:")))
classes=float(input("Classes hours:"))
study=float(input("Study hours:"))
TV=float(input("TV hours:"))
music=float(input("Music hours:"))
newdic={"Sleep":sleep, "Classes":classes, "Study":study, "TVs":TV, "Music":music, "Other":24-sleep-classes-study-TV-music}
print(newdic)