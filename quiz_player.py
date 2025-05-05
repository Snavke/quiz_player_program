# Prompt user to insert txt file to read
import tkinter as tk
from tkinter import filedialog
import json
import random


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
    for index, line in enumerate(lines_text_file):
        original_line = line
        line = line.strip()

        if "~" in line or "Created New Quiz at" in line or not line:
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
        elif current_question and line[0] in ["A", "B", "C", "D"] and "." in line:
                choice_label = line[0]
                choice_text = line.split(".", 1)[1].strip()
                quiz_information[current_question]["Choices"][choice_label] = choice_text

        # if its an answer line
        elif current_question and "Answer" in line:
            answer_part = line.split("Answer")[1].replace(":", "").strip()
            quiz_information[current_question]["Answer"] = answer_part

# Quizzes the user using the txt file
print ("\nLoading quiz...")
score = 0 

questions = list(quiz_information.keys())
# Randomized number selection
random.shuffle(questions)

for question_number in questions:
    question_data = quiz_information[question_number]
    print (f"\n{question_number}: {question_data['Question']}")
    for label, choice in question_data["Choices"].items():
        print(f"  {label}. {choice}")

    

    



 



    

    # One question at a time
    # Print score after user answers all question for a txt file. 



 # Add functionality so that user can still access previous file imported (?)

    # Multiple txt files and menu to choose which quiz to play