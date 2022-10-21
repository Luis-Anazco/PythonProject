food = {'dessert': 'Desserts', 'meals': 'Main Meals'}


dessert = {'tiramisu': 'tiramisu', 'pie': 'pie', 'pudding': 'pudding'}
meals = {'chilli': 'Chilli con carne', 'bolognaise': 'Spaghetti Bolognaise', 'bangers': 'Bangers and mash', 
'fish': 'Fish and chips'}


chilli = {'Mince beef': 800, 'Red kidney beans': 200}
bolognaise = {'Mince beef': 800, 'Tomato sauce': 800}
bangers = {'Sausages': 200, 'Mash potato': 400}
fish = {'Fish': 400, 'Chips': 200}

tiramisu = {'Cream': 400, 'Cocoa': 200}
pie = {'Strawberries': 300, 'Cream': 200}
pudding = {'Bread': 400, 'Milk': 200}


print('Hello, welcome to The LA Restaurant Recipes! You will now see a menu to choose recipes for either main meals or desserts.')


for i in meals.keys(): 
    exec("f'{meals[i]} = {i}'")

for j in food.keys(): 
    exec("f'{food[j]} = {j}'")

for d in dessert.keys():
    exec("f'{dessert[d]} = {d}'")


print('\nPlease enter the key to see the recipes for each food category. Alternatively, enter exit to exit the menu.')



while j in food.keys():
    print('\nMeal Name = Key\n')
    exec("for j in food.keys(): print(f'{food[j]} = {j}')")
    exec("menu = input('Key: ')") 
    if menu == 'exit':
        break
    elif menu == 'dessert':
        exec("for d in dessert.keys(): print(f'{dessert[d]} = {d}')")
        exec("recipe = input('Key: ')") 
        if recipe == 'exit':
            break
        exec("servings = input('Please enter the number of servings you want the recipe to be for: ')") 
        try:
            servings = int(servings)
        except ValueError:
            print('\nIncorrect value entered. Please try again.')
            continue
        if recipe == 'tiramisu':
            exec("for n in tiramisu.keys(): print(f'{n}: {servings*tiramisu[n]}g')")
            print('\nPlease choose another recipe, or alternatively, enter exit to exit the menu')
            continue
        elif recipe == 'pie':
            exec("for n in pie.keys(): print(f'{n}: {servings*pie[n]}g')")
            print('\nPlease choose another recipe, or alternatively, enter exit to exit the menu')
            continue
        elif recipe == 'pudding':
            exec("for n in pudding.keys(): print(f'{n}: {servings*pudding[n]}g')")
            print('\nPlease choose another recipe, or alternatively, enter exit to exit the menu')
            continue
        else:
            print('\nIncorrect key entered. Please try again.')
    elif menu == 'meals':
        exec("for i in meals.keys(): print(f'{meals[i]} = {i}')")
        exec("recipe = input('Key: ')") 
        if menu == 'exit':
            break
        exec("servings = input('Please enter the number of servings you want the recipe to be for: ')") 
        try:
            servings = int(servings)
        except ValueError:
            print('\nIncorrect value entered. Please try again.')
            continue
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
    else:
        print('\nIncorrect key entered. Please try again.')
