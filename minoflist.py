def min_value_in_list(data):
    m = data[0]
    i = 1
    while i < len(data):
        if data[i] < m:
            m = data[i]
        i += 1
    return m


numbers = [10, 4, 5, 6]
min_value = min_value_in_list(numbers)
print(min_value)