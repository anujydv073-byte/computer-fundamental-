import csv
import statistics
def calculate_average(marks):
    return sum(marks.values()) / len(marks)
def calculate_median(marks):
    return statistics.median(marks.values())
def find_max_score(marks):
    return max(marks.values())
def find_min_score(marks):
    return min(marks.values())
def assign_grades(marks):
    grades = {}
    for name, mark in marks.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def grade_distribution(grades):
    dist = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for g in grades.values():
        dist[g] += 1
    return dist

def pass_fail(marks):
    passed = [name for name, mark in marks.items() if mark >= 40]
    failed = [name for name, mark in marks.items() if mark < 40]
    return passed, failed

def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("----------------------------------")
    for name in marks:
        print(f"{name}\t\t{marks[name]}\t{grades[name]}")

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        mark = float(input(f"Enter marks for {name}: "))
        marks[name] = mark
    return marks

def csv_input():
    marks = {}
    file = input("Enter CSV file path (e.g. students.csv): ")
    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            name, mark = row
            marks[name] = float(mark)
    return marks

# ---------- Main CLI ----------
print("🎓 Welcome to GradeBook Analyzer 🎓")
while True:
    print("\n1. Manual Input\n2. CSV Input\n3. Exit")
    choice = input("Choose option: ")

    if choice == '1':
        marks = manual_input()
    elif choice == '2':
        marks = csv_input()
    elif choice == '3':
        print("Exiting... Goodbye ")
        break
    else:
        print("Invalid choice, try again.")
        continue

    # Analysis
    avg = calculate_average(marks)
    med = calculate_median(marks)
    maxm = find_max_score(marks)
    minm = find_min_score(marks)
    grades = assign_grades(marks)
    dist = grade_distribution(grades)
    passed, failed = pass_fail(marks)

    print_table(marks, grades)
    print(f"\n Average: {avg:.2f}, Median: {med}, Max: {maxm}, Min: {minm}")
    print(f" Grade Distribution: {dist}")
    print(f" Passed ({len(passed)}): {passed}")
    print(f"Failed ({len(failed)}): {failed}")