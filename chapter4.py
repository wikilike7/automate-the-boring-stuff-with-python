# cat_names = []
# while True:
#     print('Enter the name of cat: ')
#     name = input()
#     cat_names = cat_names + [name]
#     if name == '':
#         break
# print('The cat names are: ')
# for name in cat_names:
#     print(name)


supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


pet_name = input('Please enter cat name: ')
pet_list = ['cat', 'dog', 'fish']
if pet_name in pet_list:
    print(pet_name + ' is my pet.')
else:
    print('I do not have a pet named ' + pet_name)


