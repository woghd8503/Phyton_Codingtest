n, k = map(int, input().split())
result = 0

# N이 K이상라면 k로 계속 나누기
while n >= k:
    # N이 K이상이라면 k로 계속 나누기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n> 1:
    n -= 1
    result += 1

print(result)

'''
25 5
'''