def letters(s):
    if not s:
        return
    else:
        print(s[0])
        letters(s[1:])


word = "hello"
letters(word)
