from math import *
from datetime import *

#create a list for pantry and refigerator categories
pantryCategories = ['Canned or Jarred','Grains','Oils and Vinegar', 'Spices, Herbs, and Seasoning','Vegetables','Baking Ingredients','Sweeteners','Snacks and Cereal','Condiments',]
refrigeratorCategories = ['Dairy and Eggs', 'Vegetables','Fruits', 'Meat and Fish', 'Drinks']

#create parent lists per category in the pantry list above, and then a list within that list per common ingredients in the pantry. Within that list are the name of the ingredients and the amount
pantry = [
[['Tomatoes', 0],['Beans', 0],['Salsa', 0],['Tuna', 0],['Chicken', 0],['Sardines', 0],['Salmon', 0],['Spam', 0],['Chili', 0],['Soup', 0],['Corn', 0],['Cheese', 0],['Milk', 0],],
[['White Rice', 0],['Brown Rice', 0],['Pasta', 0],['Quinoa', 0],['Rice Noodles', 0],['Egg Noodles', 0],['Flat Bread', 0]],
[['Olive Oil', 0],['Vegetable Oil', 0],['Apple Cider Vinegar', 0],['Red Wine Vinegar', 0],['Sesame Oil', 0]],
[['Cayenne Pepper', 0],['Chili Powder', 0],['Cinnamon', 0],['Crushed Red Pepper', 0],['Garlic Powder', 0],['Salt', 0],['Oregano', 0],['Paprika', 0],[' Rosemary', 0],[' Sesame Seeds', 0],['Thyme', 0],],
[['Potatoes', 0],['Onions', 0],['Shallots', 0],['Garlic', 0],['Sweet Potatoes', 0],],
[['All Purpose Flour', 0],['Baking Soda', 0],['Baking Powder', 0],['Pure Vwanilla extract', 0],],
[['Sugar', 0],['Brown Sugar', 0],['Maple Syrup', 0],['Honey', 0],],
[['Crackers', 0],['Chips', 0],['Cookies', 0],['Biscuits', 0],['Marshmallows', 0],['Popcorn', 0],['Peanut Butter', 0],['Breakfast Cereal', 0],['Oats', 0],],
[['Ketchup', 0],['Mayo', 0],['Mustard', 0],['Hot Sauce', 0],['Soy Sauce', 0],['Fish Sauce', 0],],
]

#create  parent lists per category in the refrigerator list above, and then a list within that list per common ingredients in the refrigerator. Within that list are the name of the ingredients and the amount
refrigerator = [
[['Milk', 0],['Eggs', 0],['Shredded Cheese', 0],['Butter', 0],['Sour Cream', 0],['Cheese', 0],],
[['Lettuce', 0],['Spinach', 0],['Kale', 0],['Pepper', 0],['Button Mushrooms', 0],['Portobello Mushrooms', 0],['Shiitake Mushrooms', 0],['Green Onions', 0],],
[['Apples', 0],['Bananas', 0],['Oranges', 0],['Grapes', 0],],
[['Chicken Breast', 0],['Ground Beef',0],['Ground Turkey',0],['Salmon',0],['Shrimp',0],['Ham', 0],['Bacon', 0],['Turkey', 0]],
[['Bottled Water', 0],['Beer',0],['Red Wine',0],['White Wine',0],['Soda',0],]
]

#create functions to automatically count how many unique ingredients are in each category
pantryCategoryListCount = len(pantryCategories)
canOrJarIngredientCount = len(pantry[0])
grainsIngredientCount = len(pantry[1])
oilsAndVinegarIngredientCount = len(pantry[2])
spicesHerbsSeasoningIngredientCount = len(pantry[3])
pantryVegetablesIngredientCount = len(pantry[4])
bakingIngredientCount = len(pantry[5])
sweetenersIngredientCount = len(pantry[6])
snacksCerealIngredientCount = len(pantry[7])
condimentsIngredientCount = len(pantry[8])
refrigeratorCategoryListCount = len(refrigeratorCategories)
dairyEggsIngredientCount = len(refrigerator[0])
refrigeratorVegetablesIngredientCount = len(refrigerator[1])
fruitsIngredientCount = len(refrigerator[2])
meatFishIngredientCount = len(refrigerator[3])
drinksIngredientCount = len(refrigerator[4])

#function to prompt the user to try again if they made a mistake in their input
def tryAgain():
    print('Please try again.')

#option to choose between pantry or refrigerator 
def pantryOrRefrigerator():
    print('Pantry or Refrigerator?')
    print('1. Pantry\n')
    print('2. Refrigerator\n')
    return ''

#print out each category in the pantry
def pantryCategoriesList():
    number = 1
    for x in pantryCategories:
        print('{}.'.format(number), x)
        number += 1
    print('Enter a number for the category that you want.')
    print('Press ENTER once to add another category.')
    print('Press ENTER twice to continue.')
    return number

#function to print out a list of each ingredient in a category and their quantity plus the common unit of measure if needed.
def canOrJarredIngredientsList(pantry):
    number = 1
    for x in pantry[0]:
        print('{}.'.format(number), x[0], ': ', x[1])
        number += 1
def grainsIngredientsList(pantry):
    number = 1
    for x in pantry[1]:
        print('{}.'.format(number), x[0], ': ', x[1],'oz')
        number += 1
def oilsAndVinegarList(pantry):
    number = 1
    for x in pantry[2]:
        print('{}.'.format(number), x[0], ': ', x[1],'oz')
        number += 1  
def spicesList(pantry):
    number = 1
    for x in pantry[3]:
        print('{}.'.format(number), x[0], ': ', x[1],'oz')
        number += 1
def pantryVegetablesList(pantry):
    number = 1
    for x in pantry[4]:
        print('{}.'.format(number), x[0], ': ', x[1])
        number += 1
def bakingList(pantry):
    number = 1
    for x in pantry[5]:
        print('{}.'.format(number), x[0], ': ', x[1],'oz')
        number += 1
def sweetenerList(pantry):
    number = 1
    for x in pantry[6]:
        print('{}.'.format(number), x[0], ': ', x[1],'oz')
        number += 1
def snacksCerealList(pantry):
    number = 1
    for x in pantry[7]:
        print('{}.'.format(number), x[0], ': ', x[1])
        number += 1
def condimentList(pantry):
    number = 1
    for x in pantry[8]:
        print('{}.'.format(number), x[0], ': ', x[1])
        number += 1

#print out each category in the refigerator 
def refrigeratorCategoriesList():
    number = 1
    for x in refrigeratorCategories:
        print('{}.'.format(number), x)
        number += 1
    print('Enter a number for the category you want to add.')
    print('Press ENTER once to add another category.')
    print('Press ENTER twice to continue.')
    return number
def dairyAndEggsList(refrigerator):
    number = 1
    for x in refrigerator[0]:
        if 'cheese' in str(x).lower():
            print('{}.'.format(number), x[0], ': ', x[1], 'oz')
            number += 1
        elif 'butter' in str(x).lower():
            print('{}.'.format(number), x[0], ': ', x[1], 'oz')
            number += 1
        elif 'sour cream' in str(x).lower():
            print('{}.'.format(number), x[0], ': ', x[1], 'oz')
            number += 1
        else:
            print('{}.'.format(number), x[0], ': ', x[1], 'cartons')
            number += 1
def refrigeratorVegetablesList(refrigerator):
    number = 1
    for x in refrigerator[1]:
        print('{}.'.format(number), x[0], ': ', x[1], 'grams')
        number += 1
def fruitsList(refrigerator):
    number = 1
    for x in refrigerator[2]:
        print('{}.'.format(number), x[0], ': ', x[1], 'grams')
        number += 1
def meatAndFishList(refrigerator):
    number = 1
    for x in refrigerator[3]:
        print('{}.'.format(number), x[0], ': ', x[1], 'lbs')
        number += 1
def drinkList(refrigerator):
    number = 1
    for x in refrigerator[4]:
        print('{}.'.format(number), x[0], ': ', x[1])
        number += 1

#function to ask user the options to choose from
def AddRemoveView():
    count = 0
    while count == 0: 
        print('What would you like to do?\n')
        print('1. Add Quantity\n')
        print('2. Remove Quantity\n')
        print('3. View Ingredients\n')
        print('4. Add Unique Ingredient\n')
        print('5. Remove An Ingredient\n')
        answer = input()
        if answer.isnumeric():
            answer = int(answer)
            if answer < 1 and answer > 5:
                tryAgain()
            elif answer == 1 or answer == 2 or answer == 4 or answer == 5:
                choosePanOrRef(answer)
            elif answer == 3:
                print('Would you like to:')
                print('1. View all ingredients.')
                print('2. View from pantry or refrigerator.')
                viewAnswer = input()
                if viewAnswer == '1':
                    canOrJarredIngredientsList(pantry)
                    grainsIngredientsList(pantry)
                    oilsAndVinegarList(pantry)
                    spicesList(pantry)
                    pantryVegetablesList(pantry)
                    bakingList(pantry)
                    sweetenerList(pantry)
                    snacksCerealList(pantry)
                    condimentList(pantry)
                    dairyAndEggsList(refrigerator)
                    refrigeratorVegetablesList(refrigerator)
                    fruitsList(refrigerator)
                    meatAndFishList(refrigerator)
                    drinkList(refrigerator)
                elif viewAnswer == '2':
                    viewCount = 0
                    while viewCount == 0:
                        panOrRef = input(pantryOrRefrigerator())
                        if panOrRef.isnumeric():
                            panOrRef = int(panOrRef)
                            if panOrRef == 1:
                                viewList = viewCategories(panOrRef)
                                viewQuantity(panOrRef, viewList)
                                viewCount += 1
                            elif panOrRef == 2:
                                viewList = viewCategories(panOrRef)
                                viewQuantity(panOrRef, viewList)
                                viewCount += 1   
        else:
            tryAgain()
        doneCount = 0
        while doneCount == 0:
            done = input("Press 'Enter' to go back to main menu.")
            if done == '':
                doneCount += 1
            else:
                tryAgain()

#function to choose between pantry or refrigerator 
def choosePanOrRef(answer):
    addCount = 0
    while addCount == 0:
        panOrRef = input(pantryOrRefrigerator())
        if panOrRef.isnumeric():
            panOrRef = int(panOrRef)
            if panOrRef == 1:
                if answer == 1:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    addQuantity(panOrRef, categoriesList) 
                    addCount += 1 
                elif answer == 2:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    removeQuantity(panOrRef, categoriesList)
                    addCount += 1
                elif answer == 4:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    addUnique(panOrRef, categoriesList)
                    addCount += 1
                elif answer == 5:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    for x in categoriesList:
                        x -= 1
                        if x == 0:
                            canOrJarredIngredientsList(pantry)
                        elif x == 1:
                            grainsIngredientsList(pantry)
                        elif x == 2:
                            oilsAndVinegarList(pantry)
                        elif x == 3:
                            spicesList(pantry)
                        elif x == 4:
                            pantryVegetablesList(pantry)
                        elif x == 5:
                            bakingList(pantry)
                        elif x == 6:
                            sweetenerList(pantry)
                        elif x == 7:
                            snacksCerealList(pantry)
                        elif x == 8:
                            condimentList(pantry)
                    removeUnique(panOrRef, categoriesList)
                    addCount += 1
            elif panOrRef == 2:
                if answer == 1:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    addQuantity(panOrRef, categoriesList)
                    addCount += 1
                elif answer == 2:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    removeQuantity(panOrRef, categoriesList)
                    addCount += 1
                elif answer == 4:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    addUnique(panOrRef, categoriesList)
                    addCount += 1
                elif answer == 5:
                    categoriesList = chooseCategories(panOrRef)
                    stop = False
                    for x in categoriesList:
                        x -= 1
                        if x == 0:
                            dairyAndEggsList(refrigerator)
                        elif x == 1:
                            refrigeratorVegetablesList(refrigerator)
                        elif x == 2:
                            fruitsList(refrigerator)
                        elif x == 3:
                            meatAndFishList(refrigerator)
                        elif x == 4:
                            drinkList(refrigerator)
                    removeUnique(panOrRef, categoriesList)
                    addCount += 1
            else:
                tryAgain()
        else:
            tryAgain()       

#function to choose one or multiple categories in the pantry or refrigerator (depending on what user asked for) to add ingredient quantities to 
def chooseCategories(panOrRef):
    categoriesList = []
    Stop = False
    AddCount = 0
    if panOrRef == 1:
        typeCount = pantryCategoriesList()
        typeCount -= 1
    elif panOrRef == 2:
        typeCount = refrigeratorCategoriesList()
        typeCount -= 1
    while Stop == False:
        categories = input()
        if categories.isnumeric():
            categories = int(categories)
            if categories > 0 and categories <= typeCount:
                categoriesList.append(categories)
                AddCount += 1
            else:
                tryAgain()
        elif AddCount == 0 and categories == '':
            tryAgain()
        elif categories == '':
            Stop = True
            categoriesList = list(set(categoriesList))
            categoriesList.sort()
            return categoriesList

#function to add quantities
def addQuantity(panOrRef, categoriesList):
    for ingredientType in categoriesList:
        ingredientType -= 1
        if panOrRef == 1:
            if ingredientType == 0:
                canOrJarredIngredientsList(pantry)
                ingredientCount = canOrJarIngredientCount
            elif ingredientType == 1:
                grainsIngredientsList(pantry)
                ingredientCount = grainsIngredientCount
            elif ingredientType == 2:
                oilsAndVinegarList(pantry)
                ingredientCount = oilsAndVinegarIngredientCount
            elif ingredientType == 3:
                spicesList(pantry)
                ingredientCount = spicesHerbsSeasoningIngredientCount
            elif ingredientType == 4:
                pantryVegetablesList(pantry)
                ingredientCount = pantryVegetablesIngredientCount
            elif ingredientType == 5:
                bakingList(pantry)
                ingredientCount = bakingIngredientCount
            elif ingredientType == 6:
                sweetenerList(pantry)
                ingredientCount = sweetenersIngredientCount
            elif ingredientType == 7:
                snacksCerealList(pantry)
                ingredientCount = snacksCerealIngredientCount
            elif ingredientType == 8:
                condimentList(pantry)
                ingredientCount = condimentsIngredientCount
        elif panOrRef == 2:
            if ingredientType == 0:
                dairyAndEggsList(refrigerator)
                ingredientCount = dairyEggsIngredientCount
            elif ingredientType == 1:
                refrigeratorVegetablesList(refrigerator)
                ingredientCount = refrigeratorVegetablesIngredientCount
            elif ingredientType == 2:
                fruitsList(refrigerator)
                ingredientCount = fruitsIngredientCount
            elif ingredientType == 3:
                meatAndFishList(refrigerator)
                ingredientCount = meatFishIngredientCount
            elif ingredientType == 4:
                drinkList(refrigerator)
                ingredientCount = drinksIngredientCount
        count = 0
        stop = False
        while stop == False:
            ingredientName = input('What ingredient do you want to add (press ENTER for next or when done):\n')
            if count == 0 and ingredientName == '':
                tryAgain()
            elif count == 0 and ingredientName == '0':
                tryAgain()
            elif count > 0 and ingredientName == '':
                stop = True
            elif ingredientName.isnumeric():
                ingredientName = int(ingredientName)
                if ingredientName > 0 and ingredientName <= ingredientCount:
                    ingredientName -= 1
                    count += 1
                    quantityStop = False
                    while quantityStop == False:
                        quantity = (input('How many?: '))
                        if quantity == '' and count < 1:
                            tryAgain()
                        elif quantity.isnumeric():
                            if panOrRef == 1:
                                pantry[ingredientType][ingredientName][1] = pantry[ingredientType][ingredientName][1] + int(quantity)
                                quantityStop = True
                            elif panOrRef == 2:
                                refrigerator[ingredientType][ingredientName][1] = refrigerator[ingredientType][ingredientName][1] + int(quantity)
                                quantityStop = True
                        elif quantity == '':
                            stop = True
                else:
                    tryAgain()
            else:
                tryAgain()

#function to remove quantities
def removeQuantity(panOrRef, categoriesList):
    for ingredientType in categoriesList:
        ingredientType -= 1
        if panOrRef == 1:
            if ingredientType == 0:
                canOrJarredIngredientsList(pantry)
                ingredientCount = canOrJarIngredientCount
            elif ingredientType == 1:
                grainsIngredientsList(pantry)
                ingredientCount = grainsIngredientCount
            elif ingredientType == 2:
                oilsAndVinegarList(pantry)
                ingredientCount = oilsAndVinegarIngredientCount
            elif ingredientType == 3:
                spicesList(pantry)
                ingredientCount = spicesHerbsSeasoningIngredientCount
            elif ingredientType == 4:
                pantryVegetablesList(pantry)
                ingredientCount = pantryVegetablesIngredientCount
            elif ingredientType == 5:
                bakingList(pantry)
                ingredientCount = bakingIngredientCount
            elif ingredientType == 6:
                sweetenerList(pantry)
                ingredientCount = sweetenersIngredientCount
            elif ingredientType == 7:
                snacksCerealList(pantry)
                ingredientCount = snacksCerealIngredientCount
            elif ingredientType == 8:
                condimentList(pantry)
                ingredientCount = condimentsIngredientCount
        elif panOrRef == 2:
            if ingredientType == 0:
                dairyAndEggsList(refrigerator)
                ingredientCount = dairyEggsIngredientCount
            elif ingredientType == 1:
                refrigeratorVegetablesList(refrigerator)
                ingredientCount = refrigeratorVegetablesIngredientCount
            elif ingredientType == 2:
                fruitsList(refrigerator)
                ingredientCount = fruitsIngredientCount
            elif ingredientType == 3:
                meatAndFishList(refrigerator)
                ingredientCount = meatFishIngredientCount
            elif ingredientType == 4:
                drinkList(refrigerator)
                ingredientCount = drinksIngredientCount
        count = 0
        stop = False
        while stop == False:
            ingredientName = input('What ingredient do you want to subtract from (press ENTER for next or when done):\n')
            if count == 0 and ingredientName == '':
                tryAgain()
            elif count == 0 and ingredientName == '0':
                tryAgain()
            elif count > 0 and ingredientName == '':
                stop = True
            elif ingredientName.isnumeric():
                ingredientName = int(ingredientName)
                quantityStop = False
                if ingredientName > 0 and ingredientName <= ingredientCount:
                    ingredientName -= 1
                    count += 1
                    quantityStop = False
                    while quantityStop == False:
                        quantity = (input('How many?: '))
                        if quantity == '' and count < 1:
                            tryAgain()
                        elif panOrRef == 1:
                            if quantity > pantry[ingredientType][ingredientName][1]:
                                print('Please pick a number greater than zero and less than or equal to {}.'.format(pantry[ingredientType][ingredientName][1]))
                            elif quantity.isnumeric() and quantity > 0 and  quantity <= pantry[ingredientType][ingredientName][1]:
                                pantry[ingredientType][ingredientName][1] = pantry[ingredientType][ingredientName][1] - int(quantity)
                                quantityStop = True
                            elif quantity == '':
                                stop = True
                        elif panOrRef == 2:
                            if quantity > refrigerator[ingredientType][ingredientName][1]:
                                print('Please pick a number greater than zero and less than or equal to {}.'.format(refrigerator[ingredientType][ingredientName][1]))
                            elif quantity.isnumeric() and quantity > 0 and quantity <= refrigerator[ingredientType][ingredientName][1]:
                                refrigerator[ingredientType][ingredientName][1] = refrigerator[ingredientType][ingredientName][1] - int(quantity)
                                quantityStop = True
                            elif quantity == '':
                                stop = True

#function to view category specific quantities 
def viewCategories(panOrRef):
    viewList = []
    viewCount = 0
    stop = False
    while viewCount == 0:
        if panOrRef == 1:
            typeCount = pantryCategoriesList()
            typeCount -= 1
        if panOrRef == 2:
            typeCount = refrigeratorCategoriesList()
            typeCount -= 1
        while stop == False:
            categories = input()
            if categories.isnumeric():
                categories = int(categories)
                if categories > 0 and categories <= typeCount:
                    viewList.append(categories)
                    viewCount += 1
                else:
                    tryAgain()
            elif viewCount == 0 and categories == '':
                tryAgain()
            elif categories == '':
                stop = True
                viewList = list(set(viewList))
                viewList.sort()
                return viewList

#function to view quantities
def viewQuantity(panOrRef, viewList):
    for x in viewList:
        x -= 1
        if panOrRef == 1:
            if x == 0:
                canOrJarredIngredientsList(pantry)
            elif x == 1:
                grainsIngredientsList(pantry)
            elif x == 2:
                oilsAndVinegarList(pantry)
            elif x == 3:
                spicesList(pantry)
            elif x == 4:
                pantryVegetablesList(pantry)
            elif x == 5:
                bakingList(pantry)
            elif x == 6:
                sweetenerList(pantry)
            elif x == 7:
                snacksCerealList(pantry)
            elif x == 8:
                condimentList(pantry)
        elif panOrRef == 2:
            if x == 0:
                dairyAndEggsList(refrigerator)
            elif x == 1:
                refrigeratorVegetablesList(refrigerator)
            elif x == 2:
                fruitsList(refrigerator)
            elif x == 3:
                meatAndFishList(refrigerator)
            elif x == 4:
                drinkList(refrigerator)
        
#add a unique ingredient to the pantry or refrigerator
def addUnique(panOrRef, categoriesList,):
    for x in categoriesList:
        x -= 1
        global pantry
        global refrigerator
        if panOrRef == 1:
            newIngredient = input('What new ingredient do you want to add to Pantry:{}?:\n'.format(pantryCategories[x]))
            if x == 0:
                global canOrJarIngredientCount
                pantry[x].append([newIngredient, 0])
                canOrJarIngredientCount += 1
                canOrJarredIngredientsList(pantry)
            elif x == 1:
                global grainsIngredientCount
                pantry[x].append([newIngredient, 0])
                grainsIngredientCount += 1
                grainsIngredientsList(pantry)
            elif x == 2:
                global oilsAndVinegarIngredientCount
                pantry[x].append([newIngredient, 0])
                oilsAndVinegarIngredientCount += 1
                oilsAndVinegarList(pantry)
            elif  x == 3:
                global spicesHerbsSeasoningIngredientCount
                pantry[x].append([newIngredient, 0])
                spicesHerbsSeasoningIngredientCount += 1
                spicesList(pantry)
            elif x == 4:
                global pantryVegetablesIngredientCount
                pantry[x].append([newIngredient, 0])
                pantryVegetablesIngredientCount += 1
                pantryVegetablesList(pantry)
            elif x == 5:
                global bakingIngredientCount
                pantry[x].append([newIngredient, 0])
                bakingIngredientCount += 1
                bakingList(pantry)
            elif x == 6:
                global sweetenersIngredientCount
                pantry[x].append([newIngredient, 0])
                sweetenersIngredientCount += 1
                sweetenerList(pantry)
            elif x == 7:
                global snacksCerealIngredientCount
                pantry[x].append([newIngredient, 0])
                snacksCerealIngredientCount += 1
                snacksCerealList(pantry)
            elif x == 8:
                global condimentsIngredientCount
                pantry[x].append([newIngredient, 0])
                condimentsIngredientCount += 1
                condimentList(pantry)
        elif panOrRef == 2:
            newIngredient = input('What new ingredient do you want to add to Refrigerator:{}?:\n'.format(refrigeratorCategories[x]))
            if x == 0:
                global dairyEggsIngredientCount
                refrigerator[x].append([newIngredient, 0])
                dairyEggsIngredientCount += 1
                dairyAndEggsList(refrigerator)
            elif x == 1:
                global refrigeratorVegetablesIngredientCount
                refrigerator[x].append([newIngredient, 0])
                refrigeratorVegetablesIngredientCount += 1
                refrigeratorVegetablesList(refrigerator)
            elif x == 2:
                global fruitsIngredientCount
                refrigerator[x].append([newIngredient, 0])
                fruitsIngredientCount += 1
                fruitsList(refrigerator)
            elif x == 3:
                global meatFishIngredientCount
                refrigerator[x].append([newIngredient, 0])
                meatFishIngredientCount += 1
                meatAndFishList(refrigerator)
            elif x == 4:
                global drinksIngredientCount
                refrigerator[x].append([newIngredient, 0])
                drinksIngredientCount += 1
                drinkList(refrigerator)
        else:
            tryAgain()

#removes a unique ingredient from the pantry or refrigerator
def removeUnique(panOrRef, categoriesList):
    for x in categoriesList:
        x -= 1
        global pantry
        global refrigerator
        if panOrRef == 1:
            newIngredient = int(input('What ingredient do you want to remove from Pantry:{}?:\n'.format(pantryCategories[x])))
            newIngredient -= 1
            if x == 0:
                global canOrJarIngredientCount
                del pantry[x][newIngredient]
                canOrJarIngredientCount -= 1
                canOrJarredIngredientsList(pantry)
            elif x == 1:
                global grainsIngredientCount
                del pantry[x][newIngredient]
                grainsIngredientCount -= 1
                grainsIngredientsList(pantry)
            elif x == 2:
                global oilsAndVinegarIngredientCount
                del pantry[x][newIngredient]
                oilsAndVinegarIngredientCount -= 1
                oilsAndVinegarList(pantry)
            elif x == 3:
                global spicesHerbsSeasoningIngredientCount
                del pantry[x][newIngredient]
                spicesHerbsSeasoningIngredientCount -= 1
                spicesList(pantry)
            elif x == 4:
                global pantryVegetablesIngredientCount
                del pantry[x][newIngredient]
                pantryVegetablesIngredientCount -= 1
                pantryVegetablesList(pantry)
            elif x == 5:
                global bakingIngredientCount
                del pantry[x][newIngredient]
                bakingIngredientCount -= 1
                bakingList(pantry)
            elif x == 6:
                global sweetenersIngredientCount
                del pantry[x][newIngredient]
                sweetenersIngredientCount -= 1
                sweetenerList(pantry)
            elif x == 7:
                global snacksCerealIngredientCount
                del pantry[x][newIngredient]
                snacksCerealIngredientCount -= 1
                snacksCerealList(pantry)
            elif x == 8:
                global condimentsIngredientCount
                del pantry[x][newIngredient]
                condimentsIngredientCount -= 1
                condimentList(pantry)
        elif panOrRef == 2:
            newIngredient = int(input('What new ingredient do you want to remove from Refrigerator:{}?:\n'.format(refrigeratorCategories[x])))
            newIngredient -= 1
            if x == 0:
                global dairyEggsIngredientCount
                del refrigerator[x][newIngredient]
                dairyEggsIngredientCount -= 1
                dairyAndEggsList(refrigerator)
            elif x == 1:
                global refrigeratorVegetablesIngredientCount
                del refrigerator[x][newIngredient]
                refrigeratorVegetablesIngredientCount -= 1
                refrigeratorVegetablesList(refrigerator)
            elif x == 2:
                global fruitsIngredientCount
                del refrigerator[x][newIngredient]
                fruitsIngredientCount -= 1
                fruitsList(refrigerator)
            elif x == 3:
                global meatFishIngredientCount
                del refrigerator[x][newIngredient]
                meatFishIngredientCount -= 1
                meatAndFishList(refrigerator)
            elif x == 4:
                global drinksIngredientCount
                del refrigerator[x][newIngredient]
                drinksIngredientCount -= 1
                drinkList(refrigerator)

#starting the program on infinite loop
infiniteloop = 0
while infiniteloop == 0 :
    AddRemoveView()

