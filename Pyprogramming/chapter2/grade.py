# Grading students scores

# Get user input(numeric scores)
score = {"name": [], "subject": [], "score": []}
name = "continue"
while (name != "done"):
    name = input("Enter students name (or done to finish): ")
    subject = input("Enter the subject: ")
    score = int(input("Enter students score: "))
    if score < 0 or score > 100:
        print(f"Invalid score: {score}")
        break
    else:
        # Appending the user inputs
        score["name"].append(name)
        score["subject"].append(subject)
        score["score"].append(score)

# Grading 
# print the summary
totalStudents = len(score["name"])
totalSubjects = len(score["subject"])