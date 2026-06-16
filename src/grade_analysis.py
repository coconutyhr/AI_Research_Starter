import csv

students = {}

with open("data/students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        score = int(row["score"])
        students[name] = score

scores = students.values()

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

top_student = ""
bottom_student = ""

for name, score in students.items():
    if score == highest_score:
        top_student = name
    if score == lowest_score:
        bottom_student = name
sorted_students = sorted(students.items(), key=lambda item: item[1], reverse=True)
print("Students:", students)
print("Average score:", average_score)
print("Highest score:", highest_score)
print("Top student:", top_student)
print("Lowest score:", lowest_score)
print("Bottom student:", bottom_student)
print("Ranking:")
for rank, (name, score) in enumerate(sorted_students, start=1):
    print(rank, name, score)


with open("outputs/grade_report.txt", "w", encoding="utf-8") as file:
    file.write("Grade Analysis Report\n")
    file.write("=====================\n")
    file.write(f"Average score: {average_score}\n")
    file.write(f"Highest score: {highest_score}\n")
    file.write(f"Top student: {top_student}\n")
    file.write(f"Lowest score: {lowest_score}\n")
    file.write(f"Bottom student: {bottom_student}\n")
    file.write("\nRanking:\n")

    for rank, (name, score) in enumerate(sorted_students, start=1):
        file.write(f"{rank}. {name}: {score}\n")