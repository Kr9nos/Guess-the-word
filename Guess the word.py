#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import random

def print_cyan(text):
    print("\033[46m\033[30m" + text + "\033[0m")

def print_green(text):
    print("\033[42m\033[1;30m" + text + "\033[0m")

def print_red(text):
    print("\033[41m\033[30m" + text + "\033[0m")

print_cyan('''Welcome to "Guess the word")
The rules are simple. You will need to select the length of the word you want to guess.
For simplicity, we have decided the range of words from 4 to 6 characters.
After you have chosen the length of your word, you will receive n chances to guess the word
and 1 character will be revealed after each wrong guess for n-1 times, where n is the length of the word.
If your word's length is 4 (n = 4),the maximum number of characters you will receive is 3 (4-1 = 3).
 .''')
print()


def N(x,Root):
        n=int(x['text'])
        Root.destroy()

        if 4 <= n <= 6:
            m = str(n)
            file = m + " letter words.txt"
            with open(file, "r") as op:
                word_list = op.readline().strip().split(" ")
                word = random.choice(word_list)
                print_cyan("- " * n)
                nl = [i for i in range(n)]
                wl = ["-"] * n
                for i in range(n - 1):
                    yword = input("Type your guess: ")
                    if len(yword)!=n:
                        while len(yword)!=n:
                            yword=input('Invalid word length. Please try again: ')
                    if yword == word:
                        print_green("WIN!!\nCongratulations!! You have successfully guessed the word!!")
                        return
                    idx = random.choice(nl)
                    nl.remove(idx)
                    wl[idx] = word[idx]
                    print_cyan(" ".join(wl))
            if input() == word:
                print_green("Win!!\nCongratulations!! You have successfully guessed the word!!")
            else:
                print_red(f"Ooooh! You have used all your guesses\nThe word was: {word}")

    
def game():
        Root = tk.Tk()
        Root.title("Choose the length of the word")
        frame = tk.Frame(Root)
        frame.pack() 
        button_4 = tk.Button(frame, text="4", command=lambda:N(button_4,Root), width=10, height=3)
        button_5 = tk.Button(frame, text="5", command=lambda:N(button_5,Root), width=10, height=3)
        button_6 = tk.Button(frame, text="6", command=lambda:N(button_6,Root), width=10, height=3)
        button_4.pack(side="left", padx=50, pady=50)
        button_5.pack(side="left", padx=50, pady=50)
        button_6.pack(side="left", padx=50, pady=50)
        Root.mainloop()

def on_yes_click():
    yes_button.destroy()
    no_button.destroy()
    root.destroy()
    game()

def on_no_click():

    root.destroy()

root = tk.Tk()
root.title("So, are you ready to play")


frame = tk.Frame(root)
frame.pack()


yes_button = tk.Button(frame, text="Yes", command=on_yes_click, width=10, height=3)
yes_button.pack(side="left", padx=50, pady=50)


no_button = tk.Button(frame, text="No", command=on_no_click, width=10, height=3)
no_button.pack(side="right", padx=50, pady=50)

root.mainloop()


# In[ ]:




