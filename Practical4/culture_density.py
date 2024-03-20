a=0.05
day=0
while a<=0.9:
    day+=1
    a=a*2
print("On Day",day,"the cell density goes over 90%.")

#pseudocode comments
# Import orginal cell density(5%)
# Calculate days from zero
# Repeat while cell density is less than 90%:
#      add one day
#      cell density doubles
# When cell density is more than 90%, output the days.