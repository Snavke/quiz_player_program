# Prompt user to insert txt file to read
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Opens the file diaglog
quiz_file = filedialog.askopenfilename()

# Reads file
if quiz_file:
    with open (quiz_file, 'r') as file:
        file_content = file.read()
        print (file_content)
# Handles cancels to prevent crashes
else:
    print ("No file selected")


with open (quiz_file, "r") as file:
    for line in file:
        print (line)
    # Add functionality so that user can still access previous file imported (?)

        # Multiple txt files and menu to choose which quiz to play







# Read file

# Quizzes the user using the txt file
    # One question at a time
    # Randomized number selection
    # Print score after user answers all question for a txt file. 