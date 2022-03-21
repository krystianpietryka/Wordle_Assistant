#!/usr/bin/python3

#Script contains GUI for Wordle_Assistant
import PySimpleGUI as sg
import Wordle_Answers_For_Input

#TODO Update HELPTEXT
#TODO Cleanup this shitty code
#Update Readme.md on GitHub
#More Testing
#Test Environment

sg.theme('DarkGreen')

# Main Window
def Intro():
    layout = [[sg.Text('Welcome to Wordle Assistant!', size=(40, 1))],
              [sg.Text('Green Letters:  '), sg.InputText('', size=(2, 1), key = 'green1', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green2', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green3', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green4', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'green5', enable_events=True)],
              [sg.Text('Yellow Letters: '), sg.InputText('', size=(2, 1), key = 'yellow1', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow2', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow3', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow4', enable_events=True),
              sg.InputText('', size=(2, 1), key = 'yellow5', enable_events=True)],
              [sg.Text('Excluded Letters: '), sg.InputText('', size=(20, 1), key = 'excluded', enable_events=True)],
              [sg.Button('Display Answers') ,sg.Button('Exit'), sg.Button('Help')]]
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

    3) Excluded Input: Used for excluding words containing any of the input letters from the answer.
    Accepts letters of the english alphabet. 
    Letters do not need to be separated with spaces, for ex. "yrdau" will suffice.
    
    """)]]
    return sg.Window('Help Page', layout,  finalize=True)

# GUI Loop
def Main():
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
            green = Wordle_Answers_For_Input.Convert_Empty_Letters(values['green1'], values['green2'], values['green3'], values['green4'], values['green5'])
            yellow = Wordle_Answers_For_Input.Convert_Empty_Letters(values['yellow1'], values['yellow2'], values['yellow3'], values['yellow4'], values['yellow5'])
            print(green, yellow)
            result = Wordle_Answers_For_Input.Display_Possible_Answers(values['excluded'], green, yellow)
            
            # Valid Symbol Check
            valid_symbol_flag = 1
            for letter in yellow:
                if letter not in Wordle_Answers_For_Input.allowed_symbols:
                    valid_symbol_flag = 0
                    break
            for letter in green:
                if letter not in Wordle_Answers_For_Input.allowed_symbols:
                    valid_symbol_flag = 0
                    break

            # Display Results based on valid symbol flag
            window2 = Answers()
            if valid_symbol_flag == 1:
                result = ''.join([str(i) for i in result])
                window2['-OUTPUT-'].update(result)
            else:
                window2['-OUTPUT-'].update('Invalid Symbol Input!')
        elif event == 'Help' and not window2:
            window2 = Help()
    window.close()

if __name__ == '__main__':
    Main()