import re
import PySimpleGUI

#Scripts displays the possible 5 letter answers for given regex pattern

def Display_Possible_Answers(pattern):
    possible_answers = []
    regex_string = pattern
    with open('5_letter_words.txt', 'r') as words:
        for line in words.readlines():
            search_result = re.search(regex_string, line)
            if search_result:
                possible_answers.append(line)
    print('\n', 'Possible Answers: \n')
    for answer in possible_answers:
        print(answer)
    

Display_Possible_Answers('ho...')