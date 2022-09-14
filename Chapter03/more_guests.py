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

print('I find a bigger dinner table!')

guest_list.insert(0, 'Zhaohua Liu')
guest_list.insert(2, 'Yingze Sun')
guest_list.append('Xuewu Zhang')

print(f'{guest_list[0]}, welcome to my home for a dinner!')
print(f'{guest_list[1]}, welcome to my home for a dinner!')
print(f'{guest_list[2]}, welcome to my home for a dinner!')
print(f'{guest_list[3]}, welcome to my home for a dinner!')
print(f'{guest_list[4]}, welcome to my home for a dinner!')
print(f'{guest_list[5]}, welcome to my home for a dinner!')