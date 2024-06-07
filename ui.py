import tkinter as tk
from tkinter import scrolledtext

def display_suggestions(suggestions):
    window = tk.Tk()
    window.title("Optimization Suggestions")
    
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20, font=("Times New Roman", 12))
    text_area.pack(padx=10, pady=10)
    
    for suggestion in suggestions:
        text_area.insert(tk.END, suggestion + "\n\n")
    
    text_area.configure(state='disabled')
    
    window.mainloop()

display_suggestions(suggestions)
