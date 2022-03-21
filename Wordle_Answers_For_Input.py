import re

allowed_symbols = ['.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's','t', 'u','v', 'w', 'x', 'y','z']

def Convert_Empty_Letters(letter1, letter2, letter3, letter4, letter5):
    result = ''
    if not letter1:
        result += '.'
    else:
        result += letter1
    if not letter2:
        result += '.'
    else:
        result += letter2
    if not letter3:
        result += '.'
    else:
        result += letter3
    if not letter4:
        result += '.'
    else:
        result += letter4
    if not letter5:
        result += '.'
    else:
        result += letter5
    return result
        

#Scripts displays the possible 5 letter answers for given regex pattern
def Display_Possible_Answers(excluded_letters, green_letters_input, yellow_letters_input):
    #Convert string input to char table for all letter inputs (excluded, green, yellow)

    green_letters = []
    for letter in green_letters_input:
        if letter!= ' ':
            green_letters.append(letter)

    yellow_letters = ''
    for letter in yellow_letters_input:
        if letter != '.':
            yellow_letters += letter
    

    #Filter the 5 letter words by the letters tables
    possible_answers = []
    with open('allowed_guesses_combined.txt', 'r') as words:
        # Loop through the 5 letter words, filter by green_letters and excluded_letters
        for line in words.readlines():
            search_result = re.search(green_letters_input, line)
            #If search result matches regex, check if excluded letters are contained in the word
            possible_flag = 1 
            if search_result:
                for letter in line:
                    if letter in excluded_letters:
                        possible_flag = 0
                        break
                if possible_flag == 1:
                    possible_answers.append(line)

        # Count symbols in yellow input which are not dots, just letters
        yellow_not_dots_count = 0
        for symbol in yellow_letters:
            if symbol != '.':
                yellow_not_dots_count += 1


        answers_to_delete=[]
        # Loop through filtered answers, delete from possible answers if letters do not contain all of the yellow_letters
        for answer in possible_answers:
            for letter in yellow_letters:
                if letter not in answer:
                    if answer not in answers_to_delete:
                        answers_to_delete.append(answer)
                
        for marked_answer in answers_to_delete:
            possible_answers.remove(marked_answer)
        
        answers_to_delete.clear()
        #Exclude answers with same letter in the same index as yellow letters
        for answer in possible_answers:
            for i in range(0, 5):
                if yellow_letters_input[i] == answer[i]:
                    if answer not in answers_to_delete:
                        answers_to_delete.append(answer)
        
        #print(answers_to_delete)
        for marked_answer in answers_to_delete:
            #print(marked_answer, answers_to_delete)
            possible_answers.remove(marked_answer)
        

        # Delete wordle answers used in the past
        with open('past_answers.txt', 'r') as past_answers:
            print('\n', possible_answers)
            answers_to_delete.clear()
            for past_answer in past_answers:
                if past_answer in possible_answers:
                    print(past_answer)
                    answers_to_delete.append(past_answer)
        
        for marked_answer in answers_to_delete:
            possible_answers.remove(marked_answer)
            
    return possible_answers
    
    

