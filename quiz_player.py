# Prompt user to insert txt file to read
import tkinter as tk
from tkinter import filedialog
import json

root = tk.Tk()
root.withdraw()

# Opens the file diaglog
quiz_file = filedialog.askopenfilename()

# Reads file & Convert Json File to 

quiz_information = {}
current_question = None


with open (quiz_file, 'r') as file:
    lines_text_file = file.readlines()
    # skip header information in txt file
    for line in lines_text_file:
        line = line.strip()

        if "~" in line or "Created New Quiz at" in line:
            continue
       # Scan and detect for new question
        if line.startswith("Question"):
            current_question = line.split(":")[0].strip()
            quiz_information[current_question] = {
                "Question": line.split(":", 1)[1].strip(),
                "Choices": {},
               "Answer": ""
           }
        # if its a choice line (A, B, C, D)
        elif line and line[0] in ["A", "B", "C", "D"]:
            if "." in line:
                choice_label = line[0]
                choice_text = line.split(".", 1)[1].strip()
                quiz_information[current_question]["Choices"][choice_label] = choice_text

        # if its an answer line
        elif line.startswith("Answer"):
            answer = line.split(":", 1)[1].strip()
            quiz_information[current_question]["Answer"] = answer
            print(f"Detected answer for {current_question}: {answer}")
   


print("\nFinal quiz dictionary:\n")
print(json.dumps(quiz_information, indent=4))


    

    



 
# Handles cancels to prevent crashes


    
# Quizzes the user using the txt file
    # One question at a time
    # Randomized number selection
    # Print score after user answers all question for a txt file. 



 # Add functionality so that user can still access previous file imported (?)

    # Multiple txt files and menu to choose which quiz to play