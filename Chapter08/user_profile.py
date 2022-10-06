def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Zach', 'Xiang',
                             location='shenzhen',
                             field='finance',
                             age=30)
print(user_profile)