"""

    try-except

"""

# divmod(10,0)


try:
    divmod(10, 0)
except ZeroDivisionError as e:
    print(e)
else:
    print("pass")



