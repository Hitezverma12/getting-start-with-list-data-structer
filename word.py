def match_words(words):
    ctr = 0
    list = []
    for word in words:
          if len(words ) > 1 and word [0] == word[-1]:
               ctr += 1
               list.append(word)
    print("list of words with first and last character same \n",list)
    return ctr
count = match_words(['abc','xyz', '1221'])
print("number of words with first and last character same:",count)
