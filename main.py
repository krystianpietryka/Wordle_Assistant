#!/usr/bin/python3
import copy
import PySimpleGUI as sg
import Scripts.Wordle_Answers_For_Input as Wordle_Answers_For_Input


#Script contains GUI for Wordle_Assistant

#If incorrect symbol do not filter possible answers!
#Todo Incorporate some word usage probability??
#Update Readme.md on GitHub
#More Testing
#arrows shift input field - very important quality of life
#Disallow yellow or green input in the same letter space
#Go through help page and naming conventions to make it more user friendly
#Make display list scrollable
#make filter parameters for answer list
#TODO Cleanup this shitty code
#Optimize this shitty code
#Comment this shitty code
#Update window after clear memory to clear text_inputs
#Display some confirmation of clearing memory

sg.theme('DarkGreen')

# Main Window
def Intro():
    layout = [[sg.Text('Welcome to Wordle Assistant!', size=(40, 1))],
              [sg.Text('Green Letters:      '), sg.InputText('', size=(2, 1), key = 'green1', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green2', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green3', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green4', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green5', enable_events=True)],
              [sg.Text('Yellow Letters:     '), sg.InputText('', size=(2, 1), key = 'yellow1', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow2', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow3', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow4', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow5', enable_events=True)],
              [sg.Text('Excluded Letters: '), sg.InputText('', size=(18, 1), key = 'excluded', enable_events=True)],
              [sg.Button('Display Answers') ,sg.Button('Exit'), sg.Button('Help')],
              [sg.Button('Best Starters'), sg.Button('Clear Memory')]]
    return sg.Window('WordleAssistant', layout, finalize=True)


# Window for displaying answers, will probably add scrolling in the future
def Answers():
    layout = [[sg.Text(k='-OUTPUT-', size=(20, 50))]]
    return sg.Window('Possible Answers', layout, location=(550, 0), finalize=True)

def Help():
    layout = [[sg.Text(""" Hi! Thank you for using Wordle Assistant!

    1) Green Letters: Input known(green) letter pattern here.
    Accepts all letters of the english alphabet, and the dot used to match any character,
    but can be safely ommited, blank space will also match any character.

    2) Yellow Letters: Same as the Green Letters input, but for yellow letters (duh).

    3) Excluded Letters: Used for excluding words containing any of the input letters from the answer.
    Accepts letters of the english alphabet. 
    Letters do not need to be separated with spaces, for ex. "yrdau" will suffice.
    
    """)]]
    return sg.Window('Help Page', layout,  finalize=True)

def Best_Starters():
    layout = [[sg.Text("""The best starting guesses (according to a few internet pages) in no particular order are as follows:
    *STARE
    *IRATE
    *SOARE
    *ROATE
    *RAISE
    *SLATE
    *SAUCE
    *SHINE
    *SAUTE
    """)]]
    return sg.Window('Best Starters Page', layout,  finalize=True)

# GUI Loop
def Main():
    possible_answers_initial = []
    with open('Text_Files/allowed_guesses_combined.txt', 'r') as words:
        for line in words.readlines():
            possible_answers_initial.append(line)

    possible_answers = copy.deepcopy(possible_answers_initial)

    window1, window2 = Intro(), None
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window1:     # if closing win 1, exit program
                break
        # Call Wordle_Answers_For_Input.Display_Possible_Answers for entered pattern and excluded letters
        # Display in new popup window
        elif event == 'Display Answers' and not window2:
            green = Wordle_Answers_For_Input.Convert_Empty_Letters(values['green1'].lower(), values['green2'].lower(), values['green3'].lower(), values['green4'].lower(), values['green5'].lower())
            yellow = Wordle_Answers_For_Input.Convert_Empty_Letters(values['yellow1'].lower(), values['yellow2'].lower(), values['yellow3'].lower(), values['yellow4'].lower(), values['yellow5'].lower())
            result = Wordle_Answers_For_Input.Display_Possible_Answers(possible_answers, values['excluded'].lower(), green, yellow)
            
            # Valid Symbol Check for green and yellow letters input
            valid_symbol_flag = 1
            for letter in (green +yellow):
                if not Wordle_Answers_For_Input.Valid_Symbol_Check(letter):
                    valid_symbol_flag = 0
                    break

            # Display Results based on valid symbol flag
            window2 = Answers()
            if valid_symbol_flag == 1:
                result = 'Num of Answers: ' + str(len(possible_answers)) +'\n\n' + ''.join([str(i) for i in result])
                window2['-OUTPUT-'].update(result)
            else:
                window2['-OUTPUT-'].update('Invalid Symbol Input!')
        elif event == 'Help' and not window2:
            window2 = Help()
        elif event == 'Best Starters' and not window2:
            Best_Starters()
        elif event == 'Help' and not window2:
            window2 = Help()
        elif event == 'Clear Memory' and not window2:
            possible_answers = copy.deepcopy(possible_answers_initial)
    window.close()

if __name__ == '__main__':
    Main()