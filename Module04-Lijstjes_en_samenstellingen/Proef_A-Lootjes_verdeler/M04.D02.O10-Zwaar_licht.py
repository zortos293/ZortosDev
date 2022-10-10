from fruitmand import fruitmand
test_dict = {}
for fruit in fruitmand:
    test_dict[fruit['name']] = fruit['weight'] / 100
converted_dict = dict(sorted(test_dict.items(), key=lambda x:x[1]))
for key, value in reversed(converted_dict.items()):
    print(f"{key} {value} KG")
