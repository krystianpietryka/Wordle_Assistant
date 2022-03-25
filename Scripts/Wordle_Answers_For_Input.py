import re

def Valid_Symbol_Check(letter):
    if (letter == '.' or letter.isalpha()):
        return 1
    else:
        return 0


# This definetely can be done better
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
def Display_Possible_Answers(possible_answers, excluded_letters, green_letters_input, yellow_letters):

    answers_to_delete = []

    # Loop through the 5 letter words, filter by green_letters and excluded_letters
    for line in possible_answers:
        search_result = re.search(green_letters_input, line)
        
        #If search result matches regex, check if excluded letters are contained in the word
        if search_result:
            for letter in line:
                if letter in excluded_letters:
                    answers_to_delete.append(line)
        else:
            answers_to_delete.append(line)

    
    # Loop through filtered answers, delete from possible answers if letters do not contain all of the yellow letters
    for answer in possible_answers:
        for letter in yellow_letters:
            if letter != '.':
                if letter not in answer:
                    answers_to_delete.append(answer)
            
    #Exclude answers with same letter in the same index as yellow letters
    for answer in possible_answers:
        for i in range(0, 5):
            if yellow_letters[i] == answer[i]:
                answers_to_delete.append(answer)
    
    # Delete wordle answers used in the past
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


    return possible_answers
    
    

