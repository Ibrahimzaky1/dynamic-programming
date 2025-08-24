def all_construct(target, word_bank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in word_bank:
            if target[i:i + len(word)] == word:
                new_combinations = [sublist + [word] for sublist in table[i]]
                if i + len(word) <= len(target):
                    table[i + len(word)].extend(new_combinations)

    return table[len(target)]



print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purp']))
print(all_construct("abcdf", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("aaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  





def contains_duplicate(nums):
    seen_numbers = set()
    for num in nums:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False

print(contains_duplicate([1, 2, 3, 4]))     
print(contains_duplicate([1, 2, 3, 1]))     



def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_counts = [0] * 26 

    for i in range(len(s)):
        char_counts[ord(s[i]) - ord('a')] += 1
        char_counts[ord(t[i]) - ord('a')] -= 1

    for count in char_counts:
        if count != 0:
            return False

    return True


print(is_anagram("anagram", "nagaram"))  
print(is_anagram("rat", "car"))          
