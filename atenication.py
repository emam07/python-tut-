import tkinter as tk

from tkinter import messagebox

song = input("Enter the first song we listened to together: ")
song_words = song.split()

root = tk.Tk()
root.title("Song Checker")

def on_click():
    for word in song_words:
        if word.lower() in ["dil", "bacha", "hai"]:
            messagebox.showinfo("Result", f"Match found: {word}\nAuthentication successful!")
            return
    messagebox.showwarning("Result", "Authentication failed!")

button = tk.Button(root, text="Click Me!", command=on_click)
button.pack()

root.mainloop()
