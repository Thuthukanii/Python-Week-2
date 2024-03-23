def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(num for num in numbers if num % 2 == 0))
print("Sum of even numbers :", sum_of_even_numbers(numbers))
