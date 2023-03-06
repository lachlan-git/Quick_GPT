
from pynput.mouse import Listener, Button
from tkinter import Tk 
import pyautogui
from context_men import run_app
import sys

options_file = "process_options.txt"
#text which goes before prompt 
prompt_preamble = "You are an expert in corporate writing. When the user gives you a section of text, you are to respond with the corrected text. You will not put in any sorounding text or quotations marks. Please do not provide any coments or monolog on what you are reciving, respond with JUST the text. If you do not understand what the text is attemting to communicate respond with '???'"

def on_click(x, y, button, pressed):
    if button == Button.middle and pressed:
        # Press the "Ctrl" key
        pyautogui.keyDown('ctrl')

        # Press the "C" key
        pyautogui.press('c')

        # Release the "Ctrl" key
        pyautogui.keyUp('ctrl')

        # Pass the text in the clipboard to a function
        copy_frame = Tk()
        text = copy_frame.clipboard_get()
        
        copy_frame.destroy()

        #not great for speed, but if the user wants to modify the text this isnt bad
        my_function(text)

def read_text_file(file_name):
    # Initialize an empty dictionary to hold the data
    data_dict = {}
    with open(file_name, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            if line !="\n":
                key, value = line.strip().split(':')
                data_dict[key] = value
    return data_dict

def my_function(text):
    # Do something with the text
    x, y = pyautogui.position()

    text_processing_options = read_text_file(options_file)
    
    run_app(x, y, text, prompt_preamble, text_processing_options, listener)

with Listener(on_click=on_click) as listener:
    listener.join()
