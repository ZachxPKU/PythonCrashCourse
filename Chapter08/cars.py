def make_car(manufacturer, model, **options):
    options['manufacturer'] = manufacturer.title()
    options['model'] = model.title()

    return options


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)
