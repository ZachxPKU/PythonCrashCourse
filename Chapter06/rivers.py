rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'mississippi': 'united states',
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"\n{river.title()}")

for country in set(rivers.values()):
    print(f"\n{country.title()}")
