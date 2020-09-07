"""

    存储用户信息
        json.dump
        json.load

"""

import json

numbers = [1,2,3,4,5,6,7,8,9]

filename = 'number.json'
with open(filename, "w") as f_obj:
    json.dump(numbers, f_obj)


with open(filename) as f_obj:
    number = json.load(f_obj)

print(number)


