def can_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "t"]))
print(can_construct(
    "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]
))









def count_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == "":
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            num_ways_for_rest = count_construct(target[len(word):], word_bank, memo)
            total_count += num_ways_for_rest

    memo[target] = total_count
    return total_count


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", 'p', "ent", "enter", "ot", "o", "t"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", 
    "ee", 
    "eee",
    "eeee", 
    "eeeee",
    "eeeeee"
]))





def all_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = [[word] + way for way in suffix_ways]
            result.extend(target_ways)

    memo[target] = result
    return result



print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))





def fib(n):
    if n == 0:
        return 0
    table = [0] * (n + 2)  
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    return table[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))








def grid_traveler(m, n):
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current
            if i + 1 <= m:
                table[i + 1][j] += current

    return table[m][n]


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))




def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(target_sum + 1):
        if table[i]:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = True

    return table[target_sum]


print(can_sum(7, [2, 3]))          
print(can_sum(7, [5, 3, 4, 7]))    
print(can_sum(7, [2, 4]))          
print(can_sum(8, [2, 3, 5]))       
print(can_sum(300, [7, 14]))       
