pizzas = ['pepperoni', 'durian', 'seafood']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('beef')
friend_pizzas.append('chicken')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza.title())

print('\nMy friend\'s favorite pizzas are: ' )
for pizza in friend_pizzas:
    print(pizza.title())