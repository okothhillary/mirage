"""
This programme stores a list of products in a shopping cart
along with their prices

Author: Hillary Okoth

Version 1.0

"""
#variables to be used

options = ['1.Add item', '2.View cart', '3.Remove item', '4.Compute total', '5.Quit']
choice = 0
prices = []
cart = []
total = 0
budget = int(input('How much cash do you have: \n'))
balance = budget - total
l = 50
b = 30
o = 20
m = 10
s = 10

items = ['l', 'b', 'o', 'm', 's']

while choice != 5:
    print('Welcome to Imple-Cart!\n\nYou have the following options to make your shopping experience smooth:\n')
    for choice in options:
        print(choice)
        print()

    choice = int(input('Choose an otpion: ')) 

    if choice < 1 or choice > 5:
        print('\nNot in the options\n')

    while total < budget: 

        if choice == 1:
            item = input('What do you want to shop? ')
            cart.append(item)
            print(cart)
            price = float(input('How much does it cost? '))
            prices.append(price)
            total += price
            balance = budget - total

        elif choice == 2:

            print('Here is your cart: ')
            
            for i in range(len(cart[i])):
                print(f"{i + 1}. {cart[i]} -${price:.2f[i]}") 
            print('\nThat is it\n')

        elif choice == 3:
            item = int(input('What will you remove? '))
            item -= 1 

            if item < 0 or item > len(cart):
                print('Item does not exist')
            else:

                cart.pop(item) 
                prices.pop(item)
                print('\nremoved\n')   

        elif choice == 4:

            total = 0
            for price in prices:
                total += price
            print(f'{total:.2f}') 
    print(f'\nYour balance is ${balance}. Not enough to go on shopping\n ')

    print('Here is your receipt:\n')
    print('\n-----------------------------------------------------\n')
    for item in cart:
        print(item)
    print(f'Budget is: ${budget}')  
    print(f'Your balance is: ${balance}')  
    print('\n------------------------------------------------------\n')  

print('\nThanks for considering us\n')          


                   




    


            




