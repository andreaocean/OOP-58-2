def two_sum(numbers, targets):

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):  # начинаем с i+1, чтобы индексы не совпадали
            if nums[i] + nums[j] == target:
                return [i, j]   # возвращаем найденные индексы
    return []  # если решения нет


while True:
    nums = list(map(int, input("Enter list of numbers with space-separated:  ").split()))
    target = int(input("Enter target: "))

    print(two_sum(nums, target))

    if input("Do you want to continue? (y/n): ") == "n":
        print("Programm is finished. Bye!")
        break
