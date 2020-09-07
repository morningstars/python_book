try:
    with open("text2.txt") as file_obj:
        words = file_obj.read().split()
except FileNotFoundError as e:
    print("FileNotFoundError")
else:
    words_num = len(words)
    print(words, words_num)
