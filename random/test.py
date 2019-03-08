notes = ['new', 'look', 'american', 'courise']
search = input('What would you like to search: ')

index = notes.index(search)

if search in notes:
    print(f"The {search} is here")
else:
    print("The item is not here")

print(f'The index of {search}', index)
print('the index of {}'.format(search))