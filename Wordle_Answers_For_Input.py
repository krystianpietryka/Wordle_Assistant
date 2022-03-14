import re

allowed_symbols = ['.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's','t', 'u','v', 'w', 'x', 'y','z']

#Scripts displays the possible 5 letter answers for given regex pattern
def Display_Possible_Answers(pattern, excluded_letters_input):
    excluded_letters = []
    for letter in excluded_letters_input:
        if letter!= ' ':
            excluded_letters.append(letter)
    possible_answers = []
    regex_string = pattern
    with open('5_letter_words.txt', 'r') as words:
        for line in words.readlines():
            search_result = re.search(regex_string, line)
            #If search result matches regex, check if excluded letters are contained in the word
            possible_flag = 1 
            if search_result:
                for letter in line:
                    if letter in excluded_letters:
                        possible_flag = 0
                        break
                if possible_flag == 1:
                    possible_answers.append(line)
    return possible_answers
    