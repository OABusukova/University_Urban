grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # значение
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # ключи
dict = {}  # пустой словарь
students_sort = sorted(students)  # сортировка ключей
dict[students_sort[0]] = sum(grades[0])/len(grades[0])
dict[students_sort[1]] = sum(grades[1])/len(grades[1])
dict[students_sort[2]] = sum(grades[2])/len(grades[2])
dict[students_sort[3]] = sum(grades[3])/len(grades[3])
dict[students_sort[4]] = sum(grades[4])/len(grades[4])
print(dict)


# for key, value in dict.items():
#     print(f"{key}: {value}")




