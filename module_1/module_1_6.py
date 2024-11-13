my_dict = {'Olga': 1989, 'Dima': 1986, 'Alisa': 2015}
print('Dict: ' + str(my_dict))
print('Existing value: ' + str(my_dict['Olga']))
print('Not existing value: ' + str(my_dict.get('Alex')))
my_dict.update({'Artem': 2014, 'Andrey': 2008})
a = my_dict.pop('Artem')
print('Deleted value: ' + str(a))
print('Modified dictionary: ' + str(my_dict))

my_set = {1, 'Яблоко', 42.314}
print('Set: '+str(my_set))
my_set.update((5,6,1.6))
my_set.pop()
print('Modified set: '+str(my_set))