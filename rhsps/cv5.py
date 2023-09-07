dict1 = {
        "apples":4,
        "pears":5
         }
dict2 = {
        "bananas":8,
        "apples":7
        }
result = 0
for keys1, values1 in dict1.items():
    for keys2, values2 in dict2.items():
        if keys1 == keys2:
            result = values1 + values2
            print("After checking for matches: ", keys1, result)
