#!/usr/bin/python3
#Script contains GUI for Wordle_Assistant
import PySimpleGUI as sg
import Wordle_Answers_For_Input

sg.theme('DarkGreen')

# Main Window
def Intro():
    layout = [[sg.Text('Welcome to Wordle_Assistant!', size=(40, 1))],
              [sg.Text('Pattern:   '), sg.InputText('', size=(40, 1), key = 'pattern', enable_events=True)],
              [sg.Text('Exclude: '), sg.InputText('', size=(40, 1), key = 'excluded', enable_events=True)],
              [sg.Button('Display Answers') ,sg.Button('Exit'), sg.Button('Help')]]
    return sg.Window('WordleAssistant', layout, location=(600, 300), finalize=True)


# Window for displaying answers, will probably add scrolling in the future
def Answers():
    layout = [[sg.Text(k='-OUTPUT-', size=(20, 50))]]
    return sg.Window('Possible Answers', layout, location=(600, 0), finalize=True)


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
            result = Wordle_Answers_For_Input.Display_Possible_Answers(values['pattern'], values['excluded'])
            # Length Check
            if len(values['pattern']) != 5:
                window2 = Answers()
                window2['-OUTPUT-'].update('Pattern must be 5 letters!')
            else:
                # Valid Symbol Check
                valid_symbol_flag = 1
                for letter in values['pattern']:
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
    window.close()

if __name__ == '__main__':
    Main()