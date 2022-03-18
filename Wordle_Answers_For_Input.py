#Make this a wordle clone, not only a regex machine
#With Good letters
#     Bad Letters
#      known letters

import re

allowed_symbols = ['.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's','t', 'u','v', 'w', 'x', 'y','z']

#Scripts displays the possible 5 letter answers for given regex pattern
def Display_Possible_Answers(excluded_letters_input, green_letters_input, yellow_letters_input):
    #Convert string input to char table for all letter inputs (excluded, green, yellow)
    excluded_letters = []
    for letter in excluded_letters_input:
        if letter!= ' ':
            excluded_letters.append(letter)

    green_letters = []
    for letter in green_letters_input:
        if letter!= ' ':
            green_letters.append(letter)

    yellow_letters = []
    for letter in yellow_letters_input:
        if letter!= ' ':
            yellow_letters.append(letter)

    #Filter the 5 letter words by the letters tables
    possible_answers = []
    green_regex_string = green_letters
    with open('5_letter_words.txt', 'r') as words:

        # Loop through the 5 letter words, filter by green_letters and excluded_letters
        for line in words.readlines():
            search_result = re.search(green_regex_string, line)
            #If search result matches regex, check if excluded letters are contained in the word
            possible_flag = 1 
            if search_result:
                for letter in line:
                    if letter in excluded_letters:
                        possible_flag = 0
                        break
                if possible_flag == 1:
                    possible_answers.append(line)

        # Loop through filtered answers, delete from possible answers if letters do not contain all of the yellow_letters
        for answer in possible_answers:
            yellow_count = 0
            index_count = 0
            for letter in answer:
                if letter in yellow_letters and answer[index_count] != green_letters[index_count]:
                    yellow_count += 1
                index_count += 1
            # check if count equal to yellow letters different than .
    return possible_answers
    