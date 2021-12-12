#User input allows us to get input from a user, allows a user to input into the programme
animal = input('Do you like dogs or cats more? ') #prompt for users inside the brackets
pet_name = input('What would you name your pet? ')
print('You like {} and you would name your pet {}' .format(animal, pet_name))
apples_string = '12'
purchased_apples = input('how many apples did you buy? ')
total_apples = int(purchased_apples) + 5
print(total_apples)
friends = int(input('How many friends are you going to have over for dinner? '))
pizzas = friends * 0.5
print('You need {} pizzas to feed {} friends' .format(pizzas, friends))