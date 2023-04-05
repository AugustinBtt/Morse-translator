from tkinter import *
import pyperclip
morse_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
    'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.', '@': '.--.-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '$': '...-..-', '"': '.-..-.', '\'': '.----.', ' ': '/'
}

def text_to_morse():
    letters_list = list(text_input.get())
    low_letters = [item.lower() for item in letters_list]
    morse_output = ''
    for letter in low_letters:
        morse_output += morse_dict.get(letter, '')
        morse_output += ' '
    morse_output = morse_output.strip()

    morse_input.delete(0, END)
    morse_input.insert(0, morse_output)


def morse_to_text():
    inv_morse_dict = {v: k for k, v in morse_dict.items()} #swap keys and values of morse_dict
    letters = morse_input.get().split()
    text_output = ''
    for letter in letters:
        text_output += inv_morse_dict.get(letter, '')

    text_input.delete(0,END)
    text_input.insert(0, text_output)

def copy_morse():
    pyperclip.copy(morse_input.get())

def copy_text():
    pyperclip.copy(text_input.get())


#------------------ UI SETUP ---------------------

window = Tk()
window.title("Morse code translator")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

# Labels
text_lbl = Label(text="Text", font=("arial", 10))
text_lbl.grid(column=0, row=0, padx=10, pady=10)

morse_lbl = Label(text="Morse Code", font=("arial", 10))
morse_lbl.grid(column=0, row=1, padx=10, pady=10)

# Entries
text_input = Entry(width=30)
text_input.grid(column=1, row=0, padx=10, pady=10)

morse_input = Entry(width=30)
morse_input.grid(column=1, row=1, padx=10, pady=10)

# Buttons
to_morse = Button(text="To morse", command=text_to_morse)
to_morse.grid(column=2, row=0, padx=10, pady=10)

to_text = Button(text="To text", command=morse_to_text)
to_text.grid(column=2, row=1, padx=10, pady=10)

txt_cpy = Button(text="Copy", command=copy_text)
txt_cpy.grid(column=3, row=0, padx=10, pady=10)

morse_cpy = Button(text="Copy", command=copy_morse)
morse_cpy.grid(column=3, row=1, padx=10, pady=10)

window.mainloop()






