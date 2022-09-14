guest_list = ['Liqian Ma', 'Shiyin Wang', 'Maisang Cheng']

print(f'{guest_list[0]}, welcome to my home for a dinner!')
print(f'{guest_list[1]}, welcome to my home for a dinner!')
print(f'{guest_list[2]}, welcome to my home for a dinner!')


not_make = 'Maisang Cheng'
print(f"{not_make} can't make the dinner!")

guest_list.remove(not_make)

guest_list.append('Yangbo Li')

print(f'{guest_list[0]}, welcome to my home for a dinner!')
print(f'{guest_list[1]}, welcome to my home for a dinner!')
print(f'{guest_list[2]}, welcome to my home for a dinner!')
