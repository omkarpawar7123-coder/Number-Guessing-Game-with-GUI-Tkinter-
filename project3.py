from tkinter import *
import random

# Create window
window = Tk()

window.title("Number Guessing Game")
window.geometry("300x250")

# Random number
number = random.randint(1, 10)

# Attempt counter
attempts = 0

# Function
def check():

    global attempts

    guess = int(entry.get())

    attempts = attempts + 1

    # Show attempts
    attempt_label.config(text="Attempts: " + str(attempts))

    # Check answer
    if guess == number:
        result.config(text="Correct Guess")

    elif guess > number:
        result.config(text="Too High")

    else:
        result.config(text="Too Low")

# Heading
label = Label(window, text="Guess Number 1 to 10")
label.pack(pady=10)

# Input box
entry = Entry(window)
entry.pack(pady=10)

# Button
button = Button(window, text="Check", command=check)
button.pack(pady=10)

# Result label
result = Label(window, text="")
result.pack(pady=10)

# Attempts label
attempt_label = Label(window, text="Attempts: 0")
attempt_label.pack(pady=10)

# Run window
window.mainloop()
