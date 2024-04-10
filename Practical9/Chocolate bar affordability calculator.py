def chocolate_affordability (money,price):
    number=money//price
    change=money%price
    return number,change
money=float(input('The money you have:'))
price=float(input('The price of each chocolate：'))
number,change=chocolate_affordability(money,price)
print('You can buy',number,'chocolate bar(s) and the change is',change,'.')

# This function should be called "chocolate_affordability" in my code.