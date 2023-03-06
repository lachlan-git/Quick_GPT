
import customtkinter
from tkinter import ttk

import textwrap
import sys
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
import time

import pyautogui

import openai
import math

class App(customtkinter.CTk):
    def __init__(self, xpos, ypos, prompt, proc_options, listener):
        super().__init__()
        self.wrap_text = 80
        self.widget_width = 475
        self.proc_options = proc_options
        self.prompt = prompt

        self.listener = listener

        # configure window
        self.title("Auto GPT")
        self.geometry(f"{self.widget_width}x{200}+{xpos}+{ypos}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create a dropdown box
        self.combobox = customtkinter.CTkOptionMenu(master=self,
                                            values=list(self.proc_options.keys()),
                                            command=self.optionmenu_callback)
        
        self.combobox.grid(row=0, column=0, columnspan = 1, sticky='ew')

        self.button_X = customtkinter.CTkButton(self, command=lambda: end_program(self), text="Quit", fg_color="#808080", hover_color="#ac382d")
        self.button_X.configure(width=50)
        self.button_X.grid(row=0, column=1, padx=0, pady=2, sticky='e')

        self.prompt_text = prompt
        self.input_text = customtkinter.CTkLabel(self, text=textwrap.fill(prompt, self.wrap_text), justify="left")
        self.input_text.grid(row=1, column=0, columnspan = 2, sticky="w")
        
        self.sep = ttk.Separator(self, orient='horizontal')
        self.sep.grid(row=2, column=0, columnspan = 2, sticky="we")

        self.response = "Loading..."
        self.updated_text = customtkinter.CTkLabel(self, text=self.response, justify="left")
        self.updated_text.grid(row=3, column=0, columnspan = 2, sticky="w")

        self.button_1 = customtkinter.CTkButton(self, command=lambda: change_text(self), text="accept")
        self.button_1.grid(row=4, column=0, padx=5, pady=2, sticky='ew')
        self.button_2 = customtkinter.CTkButton(self, command=self.reject_change, text="reject", fg_color="grey", hover_color="#5A5A5A")
        self.button_2.grid(row=4, column=1, padx=5, pady=2, sticky='ew')

        self.fit_height()


    def fit_height(self):
        num_lines_text = math.ceil(len(self.prompt_text) / self.wrap_text) + math.ceil(len(self.response) / self.wrap_text)
        resize_height = min(100 + num_lines_text*15, 600)
            
        self.geometry(f"{self.widget_width}x{resize_height}")

    
        
    def optionmenu_callback(self, key):
        tranformed_text = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": self.proc_options[key]},
                        {"role": "user", "content": self.prompt}]
        )
        
        self.response = tranformed_text["choices"][0]["message"]["content"]
        self.updated_text.configure(text = textwrap.fill(self.response, self.wrap_text))

        self.fit_height()
        
        self.update()
    

    def reject_change(self):
        self.destroy()


def end_program(app):
    app.listener.stop()
    app.destroy()
    sys.exit()
    
def change_text(app):
    return_text = app.response
    app.destroy()
    time.sleep(0.25) # honestly just feels better to use with a pause here
    pyautogui.write(return_text)

def run_app(x, y, prompt, prompt_preambl, processing_options, listener):

    openai.api_key = "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"  

    app = App(x, y, prompt, processing_options, listener)
    app.update()

    tranformed_text = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt_preambl},
                  {"role": "user", "content": prompt}]
    )
    
    app.response = tranformed_text["choices"][0]["message"]["content"]
    app.updated_text.configure(text = textwrap.fill(app.response, app.wrap_text))
    app.fit_height()
    app.mainloop()





if __name__ == "__main__":
    run_app(200, 200, "what colour is the sky normally", "answer the following with 1 word", {"a":"sdd", "b":"asdf"})
