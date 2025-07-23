def foo(n):
    if n <= 1:
        return
    foo(n - 1)

def bar(n):
    if n <= 1:
        return
    bar(n - 2)

def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))




def grid_traveler(m, n, memo=None):
    if memo is None:
        memo = {}

    key = (m, n)  # using tuple instead of string for keys

    if key in memo:
        return memo[key]
    
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[key]

print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))






