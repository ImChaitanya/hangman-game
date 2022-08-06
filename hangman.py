
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):

    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    s=list(secret_word)
    return all(i in letters_guessed for i in s)

def get_guessed_word(secret_word, letters_guessed):
    global word_guessed
    word_guessed=[]
    s = list(secret_word)
    d = {}
    index = 0
    for i in range(0, len(secret_word)):
        word_guessed.append('_ ')
    for letter in s:
        if letter in d:
            d[letter].append(index)
        else:
            d[letter] = [index]
        index += 1
    for letter in letters_guessed:
        if letter in d:
            for i in range(0, len(d[letter])):
                word_guessed[d[letter][i]] = letter
    res = ''.join(word_guessed)
    return res

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    available_letters=string.ascii_lowercase
    for letter in letters_guessed:
        available_letters=available_letters.replace(letter,'')
    return available_letters

def match_with_gaps(my_word, other_word):
    s=list(other_word)
    res=False
    i=0
    if len(my_word)!=len(s):
        return res
    for letter in other_word:
        if letter in my_word:
            if my_word.count(letter)==other_word.count(letter):
                if my_word[i] == other_word[i]:
                    res = True
                else:
                    res = False
                    break
            else:
                res=False
                break
        else:
            if my_word[i] in 'abcdefghijklmnopqrstuvwxyz':
                res=False
                break
        i+=1

    return res

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    possible_matches=[]
    for word in wordlist:
        other_word=word
        if match_with_gaps(my_word,other_word):
            possible_matches.append(word)
    return possible_matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the Hangman game")
    print("I'm thinking of a word ",len(secret_word),"long")
    print("Press '*' to get hint")
    print("*********************")
    global guess
    guess=6
    warnings=3
    letters_guessed=[]
    while guess>0 and is_word_guessed(secret_word,letters_guessed)!=True:
        print('Number of guesses left: ',guess)
        print('Number of warnings left: ', warnings)
        print('Available letters: ',get_available_letters(letters_guessed))
        letter=input('Please guess a letter: ')
        if letter=='*':
            my_word=word_guessed
            print(word_guessed)
            print(show_possible_matches(my_word))
        elif letter in letters_guessed:
            print('Oops! you have already guessed that letter')
            print(get_guessed_word(secret_word,letters_guessed))
            if warnings>0:
                warnings=warnings-1
            else:
                guess=guess-1
        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                print('good guess: ',get_guessed_word(secret_word,letters_guessed))
            else:
                print('oops! that letter is not in my word: ',get_guessed_word(secret_word,letters_guessed))
                guess=guess-1

        print('*********************')
    if guess==0:
        print('Sorry ou could not guess the word')
        print('The word was: ',secret_word)
    else:
        print('Congratulaions! you guessed the word ',secret_word)

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    

