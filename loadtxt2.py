def open_txt_file():
    list_words = []
    with open("words.txt", encoding="UTF-8") as text:
        for word in text:
            list_words.append(word[:-1])
    return list_words

if __name__ == "__main__":
    print(open_txt_file())