meals = {'chilli': 'Chilli con carne', 'bolognaise': 'Spaghetti Bolognaise', 'bangers': 'Bangers and mash', 
'fish': 'Fish and chips'}

chilli = {'Mince beef': 800, 'Red kidney beans': 200}
bolognaise = {'Mince beef': 800, 'Tomato sauce': 800}
bangers = {'Sausages': 200, 'Mash potato': 400}
fish = {'Fish': 400, 'Chips': 200}


for i in meals.keys(): 
    print(f'{meals[i]} = {i}')


print('\nPlease enter the key to see the recipe for each meal. Alternatively, enter exit to exit the menu.')


while i in meals.keys():
    print('\nMeal Name = Key\n')
    exec("for i in meals.keys(): print(f'{meals[i]} = {i}')")
    exec("recipe = input('Key: ')") 
    if recipe == 'exit':
        break
    exec("servings = int(input('Please enter the number of servings you want the recipe to be for: '))")
    if recipe == 'chilli':
        exec("for n in chilli.keys(): print(f'{n}: {servings*chilli[n]}g')")
        print('\nPlease choose another recipe, or alternatively, enter exit to exit the menu')
        continue
    elif recipe == 'bolognaise':
        exec("for n in bolognaise.keys(): print(f'{n}: {servings*bolognaise[n]}g')")
        print('\nPlease choose another recipe, or alternatively, enter exit to exit the menu')
        continue
    elif recipe == 'fish':
        exec("for n in fish.keys(): print(f'{n}: {servings*fish[n]}g')")
        print('\nPlease choose another recipe, or alternatively, enter exit to exit the menu')
        continue
    elif recipe == 'bangers':
        exec("for n in bangers.keys(): print(f'{n}: {servings*bangers[n]}g')")
        print('\nPlease choose another recipe, or alternatively, enter exit to exit the menu')
        continue
    else:
        print('\nIncorrect key entered. Please try again.')

