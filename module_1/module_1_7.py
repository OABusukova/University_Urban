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