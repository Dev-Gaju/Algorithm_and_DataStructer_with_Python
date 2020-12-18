with open("python.txt", mode="r") as s_file:
    a = []
    unique_word = []
    for line in s_file.readlines():
        words = line.split(" ")
        # print(words)
        a += words
        unique_word = set(a)
    print(len(a))
    print(f"Unique word: {len(unique_word)}")
    # print(line.strip())     #end=""
