def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

info = input().split()
n = int(info[0])
target = info[1]

array = input().split()

print(sequential_search(n, target, array))
