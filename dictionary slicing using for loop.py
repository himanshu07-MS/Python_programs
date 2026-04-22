# dictionary slicing using for loop.

week = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday'}

print(id(week))                                                # refers id of week
print(type(week))                                           # refers type of week
print('keys are:',week.keys())                        # refers values of week.keys

print('values are:',week.values())                  # refers values of week.values
print('items are:',week.items())                     # refers values of week.items


print(week[1])

for i in week:
    print('Dictionary slicing are:',i)
