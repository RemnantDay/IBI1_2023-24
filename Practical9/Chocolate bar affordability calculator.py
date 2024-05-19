def chocolate_affordability (money,price): 
    """
    Determine how many chocolate bars the user is able to afford.
    Return the number of bars that can be bought and the change that will be left over.
    """                                                                                 # The head of a function
    number=money//price
    change=money%price
    return number,change
money=float(input('The money you have:'))   # Ask the user to specify the total money
price=float(input('The price of one chocolate：'))  # Ask the user to specify the price of one chocolate bar
number,change=chocolate_affordability(money,price)  #return	the	number	of	bars	that	can	be	bought	and	the	change	that	will	be	left	 over
print('You can buy',number,'chocolate bar(s) and the change is',change,'.')

# This function should be called "chocolate_affordability" in my code.
# Example (at line 16, please delete # in line 16)
#print(Chocolate_bar_affordability_calculator(100, 7))