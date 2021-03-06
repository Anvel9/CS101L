######################
##
##CS 101 Lab
## Program #1
## Anthony Velasquez
## amvmgd@umsystems.edu
##
##PROBLEM: calculate and display class grade according to weighted grade types
######################

print("**** Welcome to the LAB Grade Calculator! ****")

name=input("Who are we calculating grades for? ==> ")  ##Assigns name of student
print()

labs=int(input("Enter the Labs grade? ==> "))  ##Asking for grade inputs
if labs > 100:           ##If/elif/else statements create upper and lower input bounds
    labs = 100
    print("The lab grade value should have been 100 or less; it has been changed to 100.")
elif labs < 0:
    labs = 0
    print("The lab grade value should have been 0 or greater; it has been changed to 0.")
else:
    labs = labs
print()
        
exams=int(input("Enter the Exams grade? ==> "))
if exams > 100:
    exams = 100
    print("The exams grade value should have been 100 or less; it has been changed to 100.")
elif exams < 0:
    exams = 0
    print("The exams grade value should have been 0 or greater; it has been changed to 0.")
else:
    exams = exams
print()
    
attendance=int(input("Enter the Attendance grade? ==> "))
if attendance > 100:
    attendance = 100
    print("The attendance grade value should have been 100 or less; it has been changed to 100.")
elif attendance < 0:
    attendance = 0
    print("The attendance grade value should have been 0 or greater; it has been changed to 0.")
else:
    attendance = attendance
print()

weighted=(labs*0.7+exams*0.2+attendance*0.1)   ##Calculating overall grade as integer
print("The weighted grade for",name,"is",weighted)

if weighted < 60:                              ##Assigning letter grade to numerical grade
    letter_grade = 'F'
elif weighted < 70:
    letter_grade = 'D'
elif weighted < 80:
    letter_grade = 'C'
elif weighted < 90:
    letter_grade = 'B'
else:
    letter_grade = 'A'
    
print(name,"has a letter grade of",letter_grade)
print()
print("**** Thanks for using the LAB grade calculator ****")

