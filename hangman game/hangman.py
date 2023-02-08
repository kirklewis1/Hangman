import random
import tkinter as tk
from tkinter import messagebox

# List of words to choose from
word_list = ["python", "java", "javascript", "html", "css", "jquery", "c++", "c", "ruby", "php"]

# Initialize variables
word = random.choice(word_list)
display = ["_" for letter in word]
incorrect_letters = []
attempts = 0
MAX_ATTEMPTS = 6

# Create the main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("450x400")

# Function to handle player's guess
def guess():
    global attempts
    letter = guess_entry.get().lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        word_label.config(text="The word is: " + " ".join(display), fg="black")
        if "_" not in display:
            tk.messagebox.showinfo("You Won!", "Congratulations! You have successfully guessed the word.")
            reset()
    else:
        if letter in incorrect_letters:
            tk.messagebox.showerror("Error", "You have already tried this letter. Try another letter.")
        else:
            incorrect_letters.append(letter)
            incorrect_label.config(text="Incorrect letters: " + " ".join(incorrect_letters), fg="red")
            attempts += 1
            attempts_label.config(text="Attempts remaining: " + str(MAX_ATTEMPTS - attempts), fg="black")
        if attempts == MAX_ATTEMPTS:
            tk.messagebox.showinfo("You Lost!", "Sorry, you have used up all your attempts. The word was '" + word + "'. Better luck next time.")
            reset()

# Function to reset the game after a win or loss
def reset():
    global word, display, incorrect_letters, attempts
    word = random.choice(word_list)
    display = ["_" for letter in word]
    incorrect_letters = []
    attempts = 0
    word_label.config(text="The word is: " + " ".join(display), fg="black")
    incorrect_label.config(text="Incorrect letters: ", fg="black")
    attempts_label.config(text="Attempts remaining: " + str(MAX_ATTEMPTS - attempts), fg="black")
    guess_entry.delete(0, tk.END)

# Create the word label
word_label = tk.Label(root, text="The word is: " + " ".join(display), font=("Arial", 16), bg="lightgreen")
word_label.pack()

# Create the incorrect letters label
incorrect_label = tk.Label(root, text="Incorrect letters: ", font=("Arial", 16), bg="pink")
incorrect_label.pack()

# Create the attempts label
attempts_label = tk.Label(root, text="Attempts remaining: " + str(MAX_ATTEMPTS - attempts), font=("Arial", 16), bg="lightyellow")
attempts_label.pack()
guess_entry = tk.Entry(root, font=("Arial", 16))
guess_entry.pack()
submit_button = tk.Button(root, text="Submit", font=("Arial", 16), bg="lightblue", command=guess)
submit_button.pack()
root.mainloop()














