#!/usr/bin/python3
import PySimpleGUI as sg
import Wordle_Answers_For_Input

sg.theme('DarkGreen')


# First window
def Intro():
    layout = [[sg.Text('Welcome to Wordle_Assistant', size=(40, 1))],
              [sg.Text('Please Input Your Pattern:', size=(40, 1), key = 'pattern', enable_events=True)],
              [sg.InputText(size=(40, 1))],
              [sg.Button('Display Answers')] ,[sg.Button('Exit')]]
    return sg.Window('DiceCalculator', layout, location=(600, 300), finalize=True)

    # First window
def Answers():
    layout = [[sg.Text('Possible Answers:', size=(40, 1))],
              [sg.Text(k='-OUTPUT-', size=(40, 1))],
              [sg.Button('Exit')]]
    return sg.Window('DiceCalculator', layout, location=(600, 300), finalize=True)


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
        elif event == 'Display Answers' and not window2:
            result = Wordle_Answers_For_Input.Display_Possible_Answers(values['pattern'])
            window2 = Answers()
            window['-OUTPUT-'].update(result)

    window.close()

if __name__ == '__main__':
    Main()