def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = table[i] + [num]

    return table[target_sum]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))











def best_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    combination = table[i] + [num]
                    if table[i + num] is None or len(combination) < len(table[i + num]):
                        table[i + num] = combination

    return table[target_sum]



print(best_sum(7, [5, 3, 4, 7]))       
print(best_sum(8, [2, 3, 5]))          
print(best_sum(8, [1, 4, 5]))          
print(best_sum(100, [1, 2, 5, 25]))    





