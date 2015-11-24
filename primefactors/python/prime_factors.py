def compute(number):
    result = []
    if (1 < number):
        for value in range(2, number // 2 + 1):
            while (0 == number % value):
                result.append(value)
                number //= value
        if (not result):
            result.append(number)
    return result
