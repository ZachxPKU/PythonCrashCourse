favorate_numbers = {
    'zach' : [11, 18],
    'tim' : [16,],
    'lily' : [9, 18],
    'oliver' : [15,]
}

for name, numbers in favorate_numbers.items():
    print(f"{name.title()}'s favorate number are(is)")
    for number in numbers:
        print(number)