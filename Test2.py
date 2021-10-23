# n = int(input())
# array = []
#
# for i in range(n):
#     array.append(int(input()))
#
# array = sorted(array, reverse=True)
#
# for i in array:
#     print(i, end=' ')


# def squential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return i + 1
#
# num = input().split()
#
# n = int(num[0])
# target = num[1]
#
# array = input().split()
#
# print(squential_search(n, target, array))




# def squential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return i + 1
#
# info = input().split()
# n = int(info[0])
# target = info[1]
# array = input().split()
#
# print(squential_search(n, target, array))

# n = int(input())
# array = []
# for i in range(n):
#     array.append(int(input()))
#
# array = sorted(array, reverse = True)
#
# for i in array:
#     print(i, end=' ')

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

info = input().split()
n = int(info[0])
target = info[1]

array = input().split()

print(sequential_search(n, target, array))









