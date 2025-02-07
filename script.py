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
    return dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

def find_three_five_letter_words(words, letters):
    from itertools import combinations
    # Check if a combination of three words uses all 15 letters
    for combo in combinations(words, 3):
        if set(''.join(combo)) == set(letters) and len(''.join(combo)) == 15:
            return combo
    return None

def find_words_with_letters(words, letters):
    letters_set = set(letters)
    matching_words = [word for word in words if set(word) == letters_set]
    return matching_words

order = -1
while order !=0:
    print("""
Here's a bunch of tools to help you better your wordle game.
    MENU:
        1 - letters frequency
        2 - three words that include the top 15 letters
        3 - input five letters and find every word with the combination
        0 - exit
please enter a number: """)
    order = int(input())

    match(order):
        case 1:
            result = freqOfLetters()
            print(result)
        case 2:
            letters = list("earotlisncuydhp")  # top 15 letters
            result = find_three_five_letter_words(words_list, letters)
            if result:
                print("Three five-letter words with the top 15 letters:", result)
            else:
                print("No combination found")
        case 3:
            print("enter five letters (no spaces between them)")
            let = input()
            if (len(let) == 5):
                result = find_words_with_letters(words_list, let)
                if result:
                    print("your words are: ", result)
                else:
                    print("no matching words found")
            else:
                print("invalid input")