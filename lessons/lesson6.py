# class Money:
#     def __init__(self, amount, currency):
#         self.amount = amount
#         self.currency = currency
#
#     def __repr__(self):
#         return f"Money {self.amount}"
#
#     def __lt__(self, other):
#         return self.amount < other.amount
#
#
#     def __bool__(self):
#         return self.
#
#
#
# test = Money(100)
# test1 = Money(200)
#
# print(test)
# print(test < test1)



# class Box:
#     def __init__(self, *items):
#         self.items = list(items)
#
#     def __setitem__(self, key, value):
#         self.items[key] = value
#
#     def __getitem__(self, index):
#         return self.items[index]
#
# box = Box(1,2,3,4,5,6,7,8)
#
#
# # print(box[2])
#
#
# class Validate:
#     def __init__(self, min_len=3):
#         self.min_len = min_len
#
#     def __call__(self, s):
#         return isinstance(s, str) and len(s) >= self.min_len
#                 # сравнение
#
# is_ok = Validate(4)
# print (is_ok("12"))

def binary_search(array, target):
    left, right = 0, len(array) - 1
    count = 0

    while left <= right:
        count += 1
        print(count)
        mid = (left + right) // 2
        if array[mid] == target:
            return print("Found")
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return print("Not found")


my_array = [1,2,3,4,5,6,7,8,9,10,11]

binary_search(my_array, 6)

#Для бинарного поиска нужна последовательность
#Это главный его минус

