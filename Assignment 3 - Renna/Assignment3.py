# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Brennan Renna
# Assignment Number: Assignment 3
# Due Date: 10/10/2026
# Purpose: This program creates a GUI that converts miles per gallon into kilometers per liters
# Resources Used: Assignment 3 instructions and course materials.

#Import tkinter into the program to help set up the GUI window
import tkinter as tk

#Function to convert the MPG entered from the user to KmL
def convert_mpg(event=None):
    try:
        mpg = float(mpg_entry.get())
        km_per_liter = mpg * 0.425143707
        result_value.config(text=f"{km_per_liter:.2f}")
    except ValueError:
        result_value.config(text="")

#Creation, title and size of the window are listed for the GUI
window = tk.Tk()
window.title("MPG Converter")
window.geometry("350x200")

#Creates the label for the MPG input
mpg_label = tk.Label(window, text="Miles per Gallon: ")
mpg_label.pack()

#Creates a text box for the user to enter the input for MPG
mpg_entry = tk.Entry(window)
mpg_entry.pack()
mpg_entry.bind("<KeyRelease>", convert_mpg)

#Creates a label for the converted result in KmL
result_label = tk.Label(window, text="Kilometers per Liter: ")
result_label.pack(pady=10)

#Create a label that will display the converted answer
result_value = tk.Label(window, text="")
result_value.pack()

window.mainloop()



