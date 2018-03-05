t = "this if is you not are a reading very this good then way you have hide done a it message wrong"
print(dir(t))
help(t.split)
text = "this if is you not are a reading very this good then way you have hide done a it message wrong"
words = text.split()
for x in range(0, len(words), 2):
    print(words[x])
