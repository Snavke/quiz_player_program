# Prompt user to insert txt file to read
quiz_file = (input("Enter File Name (file.txt): "))


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