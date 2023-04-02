# print('Hello, World!')
# print('Hello again')
# print('I like typing this.')
# print('This is fun')
# print('Yay! Printing')
# print('Id much rather you "not"')
# print("i said 'do not' touch this")

# print('I will now count my chickens')

# print("Hens", 25 + 30 /6)
# print("roosters", 100 - 25 * 3 % 4)

# print("Now i will count the eggs:")

# print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# print("Is that true that 3 + 2 < 5 - 7?")

# print(3 + 2 < 5 - 7)

# print("What is 3 + 2?", 3 + 2)
# print("what is 5 - 7?", 5 - 7)

# print("Oh that's why it's false.")

# print("How about some more?")
# print("Is it greater?", 5 > -2)
# print("Is it great or equal?", 5 >= -2)
# print("Is it less or equal?", 5 <= -2)


cars = 100      # how mamy total cars
space_in_a_car = 4.0  # how much room in car
drivers = 30  # num of drivers
passengers = 30  # num of passengers
cars_not_driven = cars - drivers  # num cars not driven
cars_driven = drivers  # cars in use
carpool_capacity = cars_driven * space_in_a_car  #num of people to move
average_passengers_per_car = passengers / cars_driven #need of people to move

# print("there are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car, "in each car.")

name = 'Zachary'
age = 33
height = 74
weight = 240
eye_color = 'blue'
teeth_color = 'white'
hair_color = 'blonde'
height_in_ft = height / 12
total = age + height + weight

height_in_cm = height * 2.54
weight_in_kg = weight / 2.205


# print(f'Lets talk about {name}.')
# print(f'He is {height} inches tall ({height_in_ft}).')
# print(f'He weighs {weight} pounds. (Yeah, fat boy).')
# print(f'He has {eye_color} eyes and {hair_color} color hair.')
# print(f'His teeth are usually {teeth_color}, depending on the coffee/wine situation.')
# print(f'If you add {age}, {height}, and {weight} you get {total}')
# print(f'In england he is {height_in_cm} cm tall and weighs {weight_in_kg} kilos')


types_of_people = 10
x = f'There are {types_of_people} types of people in this world.'

binary = 'binary'
do_not = "don't"

y = f'Those that know {binary}, and those that {do_not}.'

# print(x)
# print(y)

# print(f'I said: {x}.')
# print(f'I also said: {y}.')

hilarious = False
joke_eval = "Isn't that joke so funny?! {}"

# print(joke_eval.format(hilarious))

w = 'This is the left side of a string...'

e = 'that has a right side.'

# print(w + e)

print('Mary had a little lamb.')
print('Its fleece as white as {}'.format('snow'))
print('.' * 10)

end1 = 'C'
end2 = 'H'
end3 = 'E'
end4 = 'E'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

print(end1 + end2 + end3 + end4 + end5 + end6, end = '')
print(end7 + end8 + end9 + end10 + end11 + end12)