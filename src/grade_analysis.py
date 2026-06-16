students = {
    "Alice": 85,
    "Bob": 92,
    "Cindy": 78,
    "David": 88,
    "Eva": 95
}

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