import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

def load_student_data(file_path):
    students = []
    try:
        with open(file_path, 'r') as file:
            total_students = int(file.readline().strip())
            for line in file:
                data = line.strip().split(',')
                if len(data) != 6:
                    raise ValueError(f"Invalid data format: {line.strip()}")
                student_id = int(data[0])
                name = data[1]
                coursework_marks = list(map(int, data[2:5]))
                exam_mark = int(data[5])
                students.append({
                    "id": student_id,
                    "name": name,
                    "coursework": coursework_marks,
                    "exam": exam_mark
                })
        return students
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return []
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return []

def calculate_results(student):
    total_coursework = sum(student['coursework'])
    total_marks = total_coursework + student['exam']
    percentage = (total_marks / 160) * 100
    grade = (
        'A' if percentage >= 70 else
        'B' if percentage >= 60 else
        'C' if percentage >= 50 else
        'D' if percentage >= 40 else 'F'
    )
    return total_coursework, percentage, grade

def view_all_records():
    output.delete('1.0', tk.END)
    if not students:
        output.insert(tk.END, "No student data available.\n")
        return

    total_percentage = 0
    for student in students:
        total_coursework, percentage, grade = calculate_results(student)
        output.insert(tk.END, f"Name: {student['name']}, ID: {student['id']}, "
                              f"Coursework: {total_coursework}/60, Exam: {student['exam']}/100, "
                              f"Overall: {percentage:.2f}%, Grade: {grade}\n")
        total_percentage += percentage

    average_percentage = total_percentage / len(students)
    output.insert(tk.END, f"\nTotal Students: {len(students)}, Average Percentage: {average_percentage:.2f}%\n")

def view_individual_record():
    output.delete('1.0', tk.END)
    selected_name = student_dropdown_var.get()
    if selected_name == "Select a student":
        output.insert(tk.END, "Please select a student.\n")
        return

    selected = next((student for student in students if student['name'] == selected_name), None)
    if selected:
        total_coursework, percentage, grade = calculate_results(selected)
        output.insert(tk.END, f"Name: {selected['name']}, ID: {selected['id']}\n"
                              f"Coursework: {total_coursework}/60\nExam: {selected['exam']}/100\n"
                              f"Overall: {percentage:.2f}%\nGrade: {grade}\n")
    else:
        output.insert(tk.END, "Student not found.\n")

def show_student_with_highest_score():
    output.delete('1.0', tk.END)
    if students:
        best_student = max(students, key=lambda s: sum(s['coursework']) + s['exam'])
        total_coursework, percentage, grade = calculate_results(best_student)
        output.insert(tk.END, f"Highest Scorer:\n"
                              f"Name: {best_student['name']}, ID: {best_student['id']}\n"
                              f"Coursework: {total_coursework}/60\nExam: {best_student['exam']}/100\n"
                              f"Overall: {percentage:.2f}%\nGrade: {grade}\n")
    else:
        output.insert(tk.END, "No student data available.\n")

def show_student_with_lowest_score():
    output.delete('1.0', tk.END)
    if students:
        worst_student = min(students, key=lambda s: sum(s['coursework']) + s['exam'])
        total_coursework, percentage, grade = calculate_results(worst_student)
        output.insert(tk.END, f"Lowest Scorer:\n"
                              f"Name: {worst_student['name']}, ID: {worst_student['id']}\n"
                              f"Coursework: {total_coursework}/60\nExam: {worst_student['exam']}/100\n"
                              f"Overall: {percentage:.2f}%\nGrade: {grade}\n")
    else:
        output.insert(tk.END, "No student data available.\n")

students = load_student_data('ADVANCED PROGRAMMING ASSESSMENT/students.txt')

dropdown_names = ["Select a student", "John Gabriel", "Cyruz John", "Jermyn Cayl", "Derek James", "Ricci Johnson"]

app = tk.Tk()
app.title("Student Marks Management")
app.geometry("600x600")

title_label = tk.Label(app, text="STUDENT MANAGEMENT", font=("Arial", 16))
title_label.pack(pady=10)

student_dropdown_var = tk.StringVar(app)
student_dropdown = ttk.Combobox(app, textvariable=student_dropdown_var, values=dropdown_names, state="readonly", font=("Arial", 12))
student_dropdown.set("Select a student")
student_dropdown.pack(pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

view_individual_button = tk.Button(button_frame, text="VIEW INDIVIDUAL RECORD", command=view_individual_record, 
                                   bg="blue", fg="white", font=("Arial", 12, "bold"))
view_individual_button.grid(row=0, column=0, padx=10)

highest_score_button = tk.Button(button_frame, text="SHOW HIGHEST SCORE", command=show_student_with_highest_score, 
                                 bg="blue", fg="white", font=("Arial", 12, "bold"))
highest_score_button.grid(row=0, column=1, padx=10)

lowest_score_button = tk.Button(button_frame, text="SHOW LOWEST SCORE", command=show_student_with_lowest_score, 
                                bg="blue", fg="white", font=("Arial", 12, "bold"))
lowest_score_button.grid(row=0, column=2, padx=10)

view_all_button = tk.Button(app, text="VIEW ALL STUDENT RECORDS", command=view_all_records, 
                            bg="blue", fg="white", font=("Arial", 12, "bold"))
view_all_button.pack(pady=10)

output = scrolledtext.ScrolledText(app, width=70, height=15)
output.pack(pady=10)

app.mainloop()
