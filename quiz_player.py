# Prompt user to insert txt file to read
import tkinter as tk
from tkinter import filedialog
import json
import random
import os
import time

# Add functionality so that user can still access previous file imported (?)
folder_name = "imported_quiz"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

quiz_files = [f for f in os.listdir(folder_name) if f.endswith(".json")]

print("\nSelect an Option:")
print("1. Import a new quiz")

for idx, file in enumerate(quiz_files, start = 2):
    print(f"{idx}. {file}")
print(f"{len(quiz_files)+2}. Exit")

choice = input("Enter your choice: ").strip()

if choice == "1":
    # Opens the file diaglog
    print ("Importing New Quiz", end='', flush=True)
    for msg in [" .", " ..", " ..."]:
            time.sleep(0.5)
            print(msg, end='', flush=True)
    root = tk.Tk()
    root.withdraw()
    quiz_file = filedialog.askopenfilename()
    root.destroy
    if not quiz_file:
        print ("No File Selected.")
        exit()

    quiz_information = {}
    current_question = None

    # Reads file & Convert Json File to 

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

    # Handles file duplication (adds a parenthesis with number depending on number of file occurrence)
    base_name = os.path.splitext(os.path.basename(quiz_file))[0]
    json_file_name = f"{base_name}.json"
    json_file_path = os.path.join(folder_name, json_file_name)

    if os.path.exists(json_file_path):
        base, ext = os.path.splitext(json_file_path)
        counter = 1
        while os.path.exists(f"{base})_{counter}{ext}"):
            counter += 1
        json_file_path = f"{base}_{counter}{ext}"

    # Saves the JSON structured data to JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(quiz_information, json_file, indent=4)    

    print(f"Quiz successfully saved as {os.path.basename(json_file_path)}")


elif choice.isdigit() and 2 <= int(choice) < len(quiz_files) + 2:
    selected_quiz = quiz_files[int(choice) -2]
    with open(os.path.join(folder_name, selected_quiz), 'r') as json_file:
        quiz_information = json.load(json_file)
    print (f"\nLoaded Quiz Successfully: {selected_quiz}")

else:
    print("Exiting", end='', flush=True)
    for msg in [" .", " ..", " ..."]:
            time.sleep(0.5)
            print(msg, end='', flush=True)
    exit()

# Quizzes the user using the txt file
print ("\nLoading quiz...")
user_score = 0 

questions = list(quiz_information.keys())

# Randomized number selection, one question at a time

random.shuffle(questions)

for question_number in questions:
    question_data = quiz_information[question_number]
    print (f"\n{question_number}: {question_data['Question']}")
    for label, choice in question_data["Choices"].items():
        print(f"  {label}. {choice}")

    
    user_answer = input("Answer (A, B, C, D): ").strip().lower()
    correct_answer = question_data["Answer"].strip().lower()
    RED = '\033[91m' 
    GREEN = '\033[92m' 
    RESET = '\033[0m'

    if user_answer == correct_answer:
        print (f"\n{GREEN}Correct!{RESET}")
        user_score += 1
    else: 
        print(f"\n{RED}Wrong! {RESET}The correct answer is {correct_answer}")

# Print score after user answers all question for a txt file. 
print (f"\nQuiz Completed \nYour final score: {user_score}/{len(questions)}")

    