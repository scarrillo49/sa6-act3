string_list = ["apple", "banana", "papaya", "kiwi", "orange"]

sorted_list = sorted(string_list, key=lambda x: (len(x), x))

print(sorted_list)