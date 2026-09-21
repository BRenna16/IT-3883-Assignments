#Program Name: Renna - Assignment1.py
# Course: IT3883/Section W01
# Student Name: Brennan Renna
# Assignment Number: Assignment 1
# Due Date: 09/22/2026
# Purpose: This program creates a text menu that allows a user to
# add text to an input buffer, clear the buffer, display the buffer, or exit the program.
# Resources Used: IT 3883 Course Material

# Variable used to store all text entered by the user
input_buffer = ""

# Code for the menu that repeats when prompted
while True:
    print("\n--- Input Buffer Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    choice = input("Enter your choice (1-4): ")

    # Code for option 1 to add new text to the buffer
    if choice == "1":
        new_text = input("Enter a new string to append: ")
        input_buffer += new_text
        print("Data added to the input buffer")

    # Code for option 2 to remove everything currently stored in the buffer
    elif choice == "2":
        input_buffer = ""
        print("Input buffer has been cleared.")

    # Code for option 3 to display the current contents saved in the buffer
    elif choice == "3":
        print("Current input buffer:")
        print(input_buffer)

    # Code for option 4 to terminate the program
    elif choice == "4":
        print("Exiting program.")
        break

    # Handles anything submitted besides 1-4.
    else:
        print("Invalid choice. Try again.")


