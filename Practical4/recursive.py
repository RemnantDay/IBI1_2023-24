a=4              #This sequence starts with number 4
print(a)         # Print number 4
for i in range(0,4):         #Repeat 4 times as we already have the first number.
   b=2*a+3                   #Give the new variable "b" a number according to the equation.
   print(b)                  #print the new variable
   a=b                       #Give the old variable "a" a new number so that when starting the loop again, the new variable "b" can work on this new "a".

   #pseudocode comments
   