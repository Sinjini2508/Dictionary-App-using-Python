import pandas as pd
import tkinter
from tkinter import scrolledtext

window = tkinter.Tk()
window.title("Lexica - The English Dictionary")
window.geometry("750x750")
window['bg'] = "#f09bd0"
window.resizable(width=False, height=False)


df = pd.read_csv("C:\\Users\\Sinjini\\final_list_of_words.csv")
# Importing the csv file containing the words and meaning

name_of_app = tkinter.Label(window, text="Lexica", font=("Times New Roman", 95, "bold"), bg="#f09bd0", fg="#870763")
name_of_app.place(relx = 0.5, rely = 0.1, anchor="center")
tagline = tkinter.Label(window, text="Enhance your lexical item", font=("Times New Roman", 25, "italic", "bold"), bg="#f09bd0", fg="#870763")
tagline.place(relx=0.5, rely = 0.25, anchor = "center")

search = tkinter.Label(window, text = "Search for a word", font = ("Calibri", 25, "bold"), bg="#f09bd0", fg="#25012c")
search.place(relx = 0.32, rely=0.40, anchor = "center")

search_bar = tkinter.Entry(window, font = ("Calibri", 20), fg = "#220120")
search_bar.place(relx = 0.7, rely = 0.40, anchor = "center")

def search_the_word():
    word = search_bar.get()
    word = word.title()    #Converting the word to title case because the words in the csv file are in title case
    meaning = ""
    for i in range(len(df.Word)):
        if df.Word[i].strip() == word:
            meaning += "-->" + df.Meaning[i]
            meaning += "\n\n"
            display_meaning = scrolledtext.ScrolledText(window, font = ("Calibri", 15), height=10, width=70, fg = "#220120", bg = "#f09bd0")
            display_meaning.place(relx = 0.5, rely=0.73, anchor="center")
            display_meaning.insert('end', meaning)
            display_meaning.config(state='disabled')


button_search = tkinter.Button(window, text = "Search", font=("Calibri", 20), bg="#2c0129", fg = "#ffffff", command=search_the_word)
button_search.place(relx=0.5, rely=0.50, anchor="center")


window.mainloop()


