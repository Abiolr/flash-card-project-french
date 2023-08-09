from tkinter import *
# --------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

flash_card = Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="images/card_front.png")
flash_card.create_image(400, 268, image=flash_card_front)
flash_card.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
flash_card.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
flash_card.grid(row=0, column=0, columnspan=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

window.mainloop()