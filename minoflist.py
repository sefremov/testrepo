def min_value(data):
    m = data[0]
    i = 1
    while i < len(data):
        if data[i] < m:
            m = data[i]
        i += 1
    return m


numbers = [10, 4, 5, 6]
print(min_value(numbers))