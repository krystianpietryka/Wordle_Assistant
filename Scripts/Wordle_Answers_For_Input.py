import re

# checks if values in arguments are the same char at the same index
def Same_Place_Letters_Check(green, yellow):
    for i in range(len(green)):
        if green[i].isalpha() and yellow[i].isalpha():
            return 0
    return 1

# checks if values in argument are alphabetic
def Valid_Symbol_Check(combined_inputs):
    for letter in combined_inputs:
        if not (letter == '.' or letter.isalpha()):
            return 0
    return 1

# converts empty letters in string to dots
def Convert_Empty_Letters(letters):
    result = ''
    for letter in letters:
        if not letter:
            result += '.'
        else:
            result += letter
    return result
        
# Displays the possible 5 letter answers for given regex pattern
def Display_Possible_Answers(possible_answers, excluded_letters, green_letters_input, yellow_letters):

    answers_to_delete = []

    # Loop through the 5 letter words, filter by green_letters and excluded_letters
    for line in possible_answers:
        search_result = re.search(green_letters_input, line)
        
        # If search result matches regex, mark for deletion if excluded letters are contained in the word
        if search_result:
            for letter in line:
                if letter in excluded_letters:
                    answers_to_delete.append(line)
        else:
            answers_to_delete.append(line)

    # Loop through filtered answers, mark possible answers for deletion if letters do not contain all of the yellow letters
    for answer in possible_answers:
        for letter in yellow_letters:
            if letter != '.':
                if letter not in answer:
                    answers_to_delete.append(answer)

                # If a string contains the same yellow letter and green letter
                # It must contain 2 of the same letter, so if the answer
                # does not contain 2 of the same letters, mark it for deletion
                elif letter in green_letters_input:
                    count = 0
                    for answer_letter in answer:
                        if answer_letter == letter:
                            count += 1
                    if count != 2:
                        answers_to_delete.append(answer)
            
    #Exclude answers with same letter in the same index as yellow letters
    for answer in possible_answers:
        for i in range(0, 5):
            if yellow_letters[i] == answer[i]:
                answers_to_delete.append(answer)
    
    # mark for deletion wordle answers used in the past
    with open('Text_Files/past_answers.txt', 'r') as past_answers:
        for past_answer in past_answers:
            if past_answer in possible_answers:
                answers_to_delete.append(past_answer)
    

    # Deleting answers marked for deletion
    for marked_answer in answers_to_delete:
        try:
            possible_answers.remove(marked_answer)
        except:
            pass
    possible_answers.sort()
    return possible_answers
    
    

