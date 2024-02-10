def min_cost_to_palindrome(s,k):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
        
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    if odd_count < 1:
        result[k] = 0
    else:
        result[k] = odd_count-1
    
 
test_cases = int(input())
result = {}
for i in range(test_cases):
    n = int(input())
    s = input()
    min_cost_to_palindrome(s,i)
 
for i in range(test_cases):
    print(result[i])