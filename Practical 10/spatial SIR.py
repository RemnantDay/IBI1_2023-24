# import necessary libraries
import numpy as np
import matplotlib .pyplot as plt
# make array of all susceptible population
population = np. zeros ((100,100))
outbreak = np.random.choice(range(100),2)  # Randomly select the x and y coordinates of where the outbreak is happening and store this in an array called outbreak
population[outbreak[0],outbreak[1]] = 1 # Address the person with those exact coordinates in our population array and change their status from 0 (susceptible) to 1 (infected).
plt.figure(figsize =(6,4), dpi=150)   # Determine the size of the picture
plt.imshow(population,cmap='viridis' , interpolation='nearest')
plt.title("time=0")
plt.show()        # Show the plot

N=10000            # Population Size
beta=0.3           # Beta number
gamma=0.05         # Gamma number

for t in range(101):
    # find infected points
    infectedIndex = np.where(population==1)  # Return (row, column)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (not strictly necessary)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
# Recovery
    for (i, j), value in np.ndenumerate(population):
        if value==1:  # To test whether the person is infected
            population[i,j] = np.random.choice([1,2], 1, p=[1-gamma, gamma])[0]  # If infected, there is a certain chance that he can recover


    if t==10:   # get the plot in time=10
        plt.imshow(population , cmap='viridis', interpolation='nearest')
        plt.title("time=10")
        plt.show()
    if t==50:   # get the plot in time=50
        plt.imshow(population , cmap='viridis', interpolation='nearest')
        plt.title("time=50")
        plt.show()
    if t==100:      # get the plot in time=100
        plt.imshow(population , cmap='viridis', interpolation='nearest')
        plt.title("time=100")
        plt.show()
