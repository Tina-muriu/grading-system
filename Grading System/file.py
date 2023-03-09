English=float(input("Enter English marks:"))
Maths=float(input("Enter Maths marks:"))
Chemistry=float(input("Enter Chemistry marks:"))
Physics=float(input("Enter Physics marks:"))
Computer=float(input("Enter Computer marks:"))

Total=English+Maths+Chemistry+Physics+Computer


print("Total")
print("Mean")
 
if (Mean>70):
   print("Grade A")
elif (Mean>60):
    print("Grade B")
elif (mean>50):
    print("Grade C")
elif(Mean>40):
    print("Grade D")
elif(Mean<40):
    print("Grade E")
else:
    print("Fail")
  # Define the number of students and the number of tests
num_students = 15
num_tests = 3

# Create a dictionary to hold the students' grades
grades = {}

# Prompt the user to enter the students' names and grades
for i in range(num_students):
    name = input("Enter the name of student {}: ".format(i+1))
    grades[name] = []
    for j in range(num_tests):
        grade = int(input("Enter the grade for test {}: ".format(j+1)))
        grades[name].append(grade)

# Calculate the total and mean scores for each student
for name, grade_list in grades.items():
    total = sum(grade_list)
    mean = total / num_tests
    print("{}'s total score is {} and mean score is {:.2f}".format(name, total, mean))