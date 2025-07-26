def can_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7, [2, 3]))          
print(can_sum(7, [5, 3, 4, 7]))    
print(can_sum(7, [2, 4]))          
print(can_sum(8, [2, 3, 5]))       
print(can_sum(300, [7, 14]))       










def how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            memo[target_sum] = remainder_result + [num]
            return memo[target_sum]

    memo[target_sum] = None
    return None


print(how_sum(7, [2, 3]))          
print(how_sum(7, [5, 3, 4, 7]))    
print(how_sum(7, [2, 4]))          
print(how_sum(8, [2, 3, 5]))       
print(how_sum(300, [7, 14]))       






def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination


print(best_sum(7, [5, 3, 4, 7]))     
print(best_sum(8, [2, 3, 5]))        
print(best_sum(8, [1, 4, 5]))        
