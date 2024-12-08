def data_structure(*args):
    calculate_structure_sum = []
    if data_structure() > 0:
        sum(len(data_structure()))
        calculate_structure_sum.append(data_structure())
    return calculate_structure_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
