# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

pizzas = ['pepperoni', 'neapolitan', 'sicilian', 'margherita', 'quattro formaggi']

friend_pizzas = pizzas[:]

pizzas.append("new york")
friend_pizzas.append("detroit")

print("\nthis is my favorite pizzas")
for pizza in pizzas:
    print(pizza)


print("\nthis is my friend's favorite pizzas")
for pizza in friend_pizzas:
    print(pizza)


