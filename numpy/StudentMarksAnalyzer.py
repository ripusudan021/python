import numpy as np

stu = int(input("Enter Total Number of Student: "))
sub = int(input("Enter Number of Subject: "))

studentName = []
studentMarks = []
for i in range(stu):
    name = input(f"Enter Student {i+1} Name: ")
    studentName.append(name)
    marks = []
    for j in range(sub):
        mark = int(input(f"Enter Marks of Subject {j+1}: "))
        marks.append(mark)
    studentMarks.append(marks)

students = np.array(studentName)
marks = np.array(studentMarks)

# Statistics
percentage = np.mean(marks, axis=1)
average = np.mean(percentage, axis=0)
highest = np.max(percentage)
lowest = np.min(percentage)
std = np.std(percentage)

# Above average
above_average = percentage > average

# Ranking
ranking = np.argsort(percentage)[::-1]

#grading
grades = np.where(percentage >= 90, 'A+',
         np.where(percentage >= 80, 'A',
         np.where(percentage >= 70, 'B',
         np.where(percentage >= 60, 'C',
         np.where(percentage >= 50, 'D', 'F')))))

#Subject Toper
subTopper = np.argmax(marks, axis=0)

print("========================================\n STUDENT MARKS ANALYZER\n========================================")

print("Students: ",stu)
print("Subjects: ",sub)

print("------------- CLASS STATISTICS ----------")
print(f"Average Marks : {average:.2f}")
print(f"Highest Marks : {highest:.2f}%")
print(f"Lowest Marks  : {lowest:.2f}%")
print(f"Std Deviation : {std:.2f}")

print("--------------- RANKING -----------------")

print(f"Rank  Student  Percentage  Grade")           
for rank, index in enumerate(ranking, start=1):
    print(f"{rank}  {students[index]}  {percentage[index]:.2f}%  {grades[index]}")

print("------------- ABOVE AVERAGE -------------")

for name in students[above_average]:
    print(f"{name}")


print("------------- SUBJECT TOPPERS -----------")

for index, name in enumerate(students[subTopper],start=1):
    print(f"Subject {index} Topper : {name}")
    
    