

example = 'Топинамбур'
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1::2])

print("'module_1_4.py'")
print('Введите текст: ')
my_string = input()
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])

print("'module_1_5.py'")
immutable_var = ('a', 'b', 1, 2, 'true')
print(immutable_var)
mutable_list = ['a', 'b', 1, 2, 'true']
print(mutable_list)
mutable_list[1] = 150
print(mutable_list)

print('module_1_6.py')
my_dict = {'Olga': 1989, 'Dima': 1986, 'Alisa': 2015}
print('Dict: ' + str(my_dict))
print('Existing value: ' + str(my_dict['Olga']))
print('Not existing value: ' + str(my_dict.get('Alex')))
my_dict.update({'Artem': 2014, 'Andrey': 2008})
a = my_dict.pop('Artem')
print('Deleted value: ' + str(a))
print('Modified dictionary: ' + str(my_dict))

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # значение
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # ключи
dict = {}  # пустой словарь
dict.update({'Aaron': [5, 3, 3, 5, 4], 'Bilbo': [2, 2, 2, 3], 'Johny': [4, 5, 5, 2], 'Khendrik': [4, 4, 3],
             'Steve': [5, 5, 5, 4, 5]})  # добавила значения в пустой словарь
Aaron = [5, 3, 3, 5, 4]
Bilbo = [2, 2, 2, 3]
Johny = [4, 5, 5, 2]
Khendrik = [4, 4, 3]
Steve = [5, 5, 5, 4, 5]
dict['Aaron'] = (sum(Aaron) / len(Aaron))
dict['Bilbo'] = (sum(Bilbo) / len(Bilbo))
dict['Johny'] = (sum(Johny) / len(Johny))
dict['Khendrik'] = (sum(Khendrik) / len(Khendrik))
dict['Steve'] = (sum(Steve) / len(Steve))
print(dict)
