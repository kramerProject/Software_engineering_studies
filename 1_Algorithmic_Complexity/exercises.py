# time and space complexity O(n)
def squared_array(numbers):
    squares = []
    for number in numbers:
        squares.append(number * number)
    return squares

# time complexity O(n) and space complexity O(1)
def multiply_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# time and space complexity O(n2)
def multiply_arrays(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result

# time and space complexity O(n3)
def multiply_arrays_n3(array1, array2, array3):
    result = []
    for number1 in array1:
        for number2 in array2:
            for number3 in array3:
                result.append(number1 + number2 + number3)

    return result


numbers = [1,2]
print(squared_array(numbers))
print(multiply_numbers(numbers))
print(multiply_arrays(numbers, numbers))
print(multiply_arrays_n3(numbers, numbers, numbers))