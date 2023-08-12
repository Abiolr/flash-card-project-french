from tkinter import *
import pandas
import random
# french version of project
# --------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------- OPEN FILE AND EXCEPTION HANDLING ------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")

# --------------------------- VARIABLES ------------------------------- #
data_list = data.to_dict(orient="records")
words_to_learn_list = []
french_word = ""
english_word = ""

# --------------------------- FUNCTIONS ------------------------------- #
def flip_card(french_word_index):
    """
    - passes the index of the french word to get the english translation
    - flips the card with the english translation on the other side
    - sets the right and wrong button to NORMAL
    """
    global french_word
    global english_word
    english_translation = data_list[french_word_index]["English"]
    flash_card.itemconfig(flash_card_img, image=flash_card_back)
    flash_card.itemconfig(title_text, text=f"English", fill="white")
    flash_card.itemconfig(word_text, text=f"{english_translation}", fill="white")
    french_word = data_list[french_word_index]['French']
    english_word = english_translation
    right_button.config(state=NORMAL)
    wrong_button.config(state=NORMAL)

def next_card():
    """
    - called at the beginning of program
    - goes to the next card (shows french translation of word)
    - sets the right and wrong button to DISABLED
    - calls the flip_card function after 3 seconds
    """
    random_index = random.randint(0, len(data_list) - 1)
    random_french_word = data_list[random_index]['French']
    flash_card.itemconfig(flash_card_img, image=flash_card_front)
    flash_card.itemconfig(title_text, text=f"French", fill="black")
    flash_card.itemconfig(word_text, text=f"{random_french_word}", fill="black")
    right_button.config(state=DISABLED)
    wrong_button.config(state=DISABLED)
    window.after(3000, flip_card, random_index)

def right():
    """
    - called when right button is pressed
    - removes word from list
    - closes window if list is empty
    - calls next_card function
    """
    data_list.remove({"French": french_word, "English": english_word})
    if {"French": french_word, "English": english_word} in words_to_learn_list:
        words_to_learn_list.remove({"French": french_word, "English": english_word})
    if len(data_list) == 0:
        window.destroy()
    next_card()

def wrong():
    """
    - called when wrong button is pressed
    - adds word to list
    - calls next_card function
    """
    global french
    global english
    if {"French": french_word, "English": english_word} not in words_to_learn_list:
        words_to_learn_list.append({"French": french_word, "English": english_word})
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

flash_card = Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="images/card_front.png")
flash_card_back = PhotoImage(file="images/card_back.png")
flash_card_img = flash_card.create_image(400, 268, image=flash_card_front)
title_text = flash_card.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = flash_card.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
flash_card.grid(row=0, column=0, columnspan=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=right)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=wrong)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()

# Adding incorrect words to new file
for words_remaining in data_list:
    if words_remaining not in words_to_learn_list:
        words_to_learn_list.append(words_remaining)
words_to_learn = pandas.DataFrame(words_to_learn_list)
words_to_learn.to_csv("data/words_to_learn.csv", index=False)