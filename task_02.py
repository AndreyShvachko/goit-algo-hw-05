def binary_search_with_upper_bound(arr, target):
    """
    Реалізація двійкового пошуку для відсортованого масиву дробових чисел.
    Повертає кількість ітерацій та найменший елемент, більший або рівний заданому target.
    """
    left, right = 0, len(arr) - 1  # Ініціалізуємо початкові межі пошуку
    iterations = 0
    upper_bound = None  # Змінна для зберігання найменшого елемента, більшого або рівного target

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        print(f"Ітерація {iterations}: left={left}, right={right}, mid={mid}")

        if arr[mid] >= target:
            upper_bound = arr[mid]  # Зберігаємо як потенційну верхню межу
            right = mid - 1         # Продовжуємо пошук у лівій частині
        else:
            left = mid + 1          # Шукаємо далі у правій частині

    print(f"Знайдено за {iterations} ітерацій.")
    return (iterations, upper_bound)

# Тестуємо функцію:
arr = [1.1, 2.3, 3.5, 4.7, 6.0, 7.2, 8.8, 9.9]
target = 5.0

result = binary_search_with_upper_bound(arr, target)
print(f"Кількість ітерацій: {result[0]}, Вер хня межа: {result[1]}")
