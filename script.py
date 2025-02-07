def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words_list = [line.strip() for line in file]
    return words_list
words_list = words_list = read_words_from_file("words.txt")

def freqOfLetters():
    res = {
        'a':0 , 'b':0 , 'c':0 , 'd':0 , 'e':0 , 'f':0 , 'g':0 , 'h':0 , 'i':0 , 'j':0 , 'k':0 , 'l':0 , 'm':0 , 'n':0 , 'o':0 , 'p':0 , 'q':0 , 'r':0 , 's':0 , 't':0 , 'u':0 , 'v':0 , 'w':0 , 'x':0 , 'y':0 , 'z':0 
    }
    for word in words_list:
        for let in word:
            for l in res:
                if l == let:
                    res[l] += 1
    print(dict(sorted(res.items(), key=lambda item: item[1], reverse=True)))

def find_three_five_letter_words(words, letters):
    from itertools import combinations
    # Check if a combination of three words uses all 15 letters
    for combo in combinations(words, 3):
        if set(''.join(combo)) == set(letters) and len(''.join(combo)) == 15:
            return combo
    return None

letters = list("earotlisncuydhp")  # top 15 letters

result = find_three_five_letter_words(words_list, letters)

if result:
    print("Three five-letter words:", result)
else:
    print("No combination found")

freqOfLetters()