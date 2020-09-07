import json

# username = input("your name:")

filename = "username.json"

# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("we will remember your name:" + username)
#
#
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("welcome back ", username)


try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("your name:")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we will remember your name:" + username)
else:
    print("welcome back:", username)
