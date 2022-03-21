#!/usr/bin/python3

#Script contains GUI for Wordle_Assistant
import PySimpleGUI as sg
import Wordle_Answers_For_Input


#TODO Divide input fields into single squares
#TODO Update HELPTEXT
#TODO a check to prevent yellow letters len lesser than 5
#TODO Cleanup this shitty code

sg.theme('DarkGreen')

# Main Window
def Intro():
    layout = [[sg.Text('Welcome to Wordle Assistant!', size=(40, 1))],
              [sg.Text('Green Letters: '), sg.InputText('', size=(40, 1), key = 'green', enable_events=True)],
              [sg.Text('Yellow Letters: '), sg.InputText('', size=(40, 1), key = 'yellow', enable_events=True)],
              [sg.Text('Excluded Letters: '), sg.InputText('', size=(40, 1), key = 'excluded', enable_events=True)],
              [sg.Button('Display Answers') ,sg.Button('Exit'), sg.Button('Help')]]
    return sg.Window('WordleAssistant', layout, finalize=True)


# Window for displaying answers, will probably add scrolling in the future
def Answers():
    layout = [[sg.Text(k='-OUTPUT-', size=(20, 50))]]
    return sg.Window('Possible Answers', layout, location=(550, 0), finalize=True)

def Help():
    layout = [[sg.Text(""" Hi! Thank you for using Wordle Assistant!

    1) Pattern Input: Input known/unknown letters pattern here.
    Accepts letters of the english alphabet, and the
    "." symbol, used for matching any letter. Input must be 5 symbols long.

    2) Excluded Input: Used for excluding words containing any of the input letters from the answer.
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
            result = Wordle_Answers_For_Input.Display_Possible_Answers(values['excluded'], values['green'], values['yellow'])
            # Length Check
            if (len(values['green']) != 5):
                window2 = Answers()
                window2['-OUTPUT-'].update('Green Pattern must be 5 letters!')
            else:
                # Valid Symbol Check
                valid_symbol_flag = 1
                for letter in values['yellow']:
                    if letter not in Wordle_Answers_For_Input.allowed_symbols:
                        valid_symbol_flag = 0
                        break
                for letter in values['green']:
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