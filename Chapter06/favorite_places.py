favorite_places = {'zach': ['shanghai', 'shenzhen', 'london'],
                   'oliver': ['beijing', 'guangzhou'],
                   'charlie': ['hangzhou', 'wuhan']}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")