student = {
    "name": "Ricky",
    "math": 85,
    "english": 0,
    "python": 0
}

def calculate_student_average(student):
    scores = [
        student["math"],
        student["english"],
        student["python"]
    ]
    return sum(scores) / len(scores)

def student_report(student):
    average = calculate_student_average(student)
    if average >= 60:
        result = "成績合格"
    else:
        result = "成績不及格"
    
    return f"{student['name']}的平均分數是:{average:.2f}，{result}"


    

print(student_report(student))