from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}


def draw_letters():
    # list of available letters
    letter_pool_list = []

    # letter shows up according to its count 
    for letter in LETTER_POOL:
        count = LETTER_POOL[letter]
        for copy in range(count):
            letter_pool_list.append(letter)

	#print(letter_pool_list)
	
    # randomly drawn letters 
    letter_bank = []

    # loops until 10 letters
    while len(letter_bank) < 10:
        random_index = randint(0, len(letter_pool_list) - 1)
        drawn_letter = letter_pool_list[random_index]
        # remove from pool list to not draw again
        letter_pool_list.remove(drawn_letter)
        # then add it to bank to show user
        letter_bank.append(drawn_letter)

    return letter_bank

#print(letter_bank)

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass