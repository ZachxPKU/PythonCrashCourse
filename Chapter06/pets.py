pets = []

pet = {
    'animal type': 'dog',
    'name': 'charlie',
    'owner': 'zach',
    'weight': 65,
    'eats': 'rice',
}

pets.append(pet)

pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}

pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}

pets.append(pet)

for pet in pets:
    print(pet)