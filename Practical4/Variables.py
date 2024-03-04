a=40
b=36
c=30
d=a-b
e=b-c
print(d>e)
print(d<e)
print(d==e)
if d>e:
    print("Running only had a greater improvement on running time.")
elif d<e:
    print("Running and strength training had a greater improvement on running time.")
else:
    print("They had the same effect")
# By running this code, I can see that using a combination of running and strength exercises had a greater improvement on running time.

X=True
Y=False
W=X or Y
print(W)
# W is true.
