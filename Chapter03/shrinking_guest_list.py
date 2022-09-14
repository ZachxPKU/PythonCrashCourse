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

print("I find out that my new dinner table won’t arrive in time for the dinner,"
      " and I have space for only two guests.")

not_make = guest_list.pop()
print(f"Sorry, {not_make}! I can not invite you to my home for dinner!")
not_make = guest_list.pop()
print(f"Sorry, {not_make}! I can not invite you to my home for dinner!")
not_make = guest_list.pop()
print(f"Sorry, {not_make}! I can not invite you to my home for dinner!")
not_make = guest_list.pop()
print(f"Sorry, {not_make}! I can not invite you to my home for dinner!")

print(f'{guest_list[0]}, welcome to my home for a dinner!')
print(f'{guest_list[1]}, welcome to my home for a dinner!')

del guest_list[0]
del guest_list[0]
print(guest_list)