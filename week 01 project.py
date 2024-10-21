#Project  week 01 - Student Management System
 
#Objective: Create a basic Student Management System that uses the concepts learned throughout the week. This project will involve adding, viewing, and managing student information like names, ages, and grades. The project will cover input/output, control structures, loops, functions, and lists. Each day will build on the previous concepts to complete a functional system.
class Students: #creating a class Students
    def __init__(self): #define an method for the class
        #Create a program that asks the user to input a student's name, age, and roll no, subjects enrolled. And store this information in a list or dictionary.
        self.name = input('enter the student name')
        self.age = int(input('enter the student age'))
        self.gender = input('enter the gender of the student')
        self.ID = int(input('enter the student ID'))
        self.subjects = [subject.strip() for subject in input('Enter the subjects allocated for this student separated by commas: ').split(',')]  # Create a list of subjects
        self.scores = []
        self.input_scores()
        
    def input_scores(self): #initializing a new method for scores
        for subjects in self.subjects:
            score = float(input(f'enter the scores for {subjects}:')) #collecting scores for each subject
            self.scores.append(score)
            
    def display_information(self): #initializing another method to display the information
        print('the information of the students are given below')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
        print(f'ID: {self.ID}')
        for subject, score in zip(self.subjects, self.scores):
            print(f'Subject: {subject}, Score: {score}')
        
        #ask the user if they want to calculate the scores and display their grade?
        choice = input('do you want to calculate the scores and display the grade results?: yes, no')
        if choice == 'yes':
            for grade in self.scores:
                

        
        else:
            print('exiting the program')

# Create instance of the Students class and display information
student = Students()
student.display_information()

# Implement a feature that performs basic arithmetic operations on the student’s grades (e.g., adding test scores).
 
# Allow the user to calculate the student's total score from multiple tests.
 
#3. Grade Calculation - Extend the program to calculate grades based on marks entered by the user. Use the following criteria: Marks >= 90: A,  Marks 7589: B,  Marks 5074: C,   Marks < 50: Fail,  Print the student's name along with their grade.
 
# 2. Pass/Fail Classification - Ask the user to input marks for a student. Use conditional statements to check if the student has passed or failed. Print “Passed” or “Failed” based on the grade.
 
#1. Calculate Average Marks - Write a program that allows the user to input a student’s marks for 5 subjects.
 
#Calculate and print the student’s average marks using a loop.
 
#2. List Students Who Passed - Use a loop to go through a list of students and print the names of those who passed (marks >= 50).
 
#Ensure that the program can handle any number of students and subjects.
 
#1. Modularize the Program - Refactor your student management system by breaking the code into functions (e.g., one function for adding students, one for grading, etc.).
 
#Create functions to: Add a student. View all students. Calculate and return a student’s grade based on their marks. Calculate the average marks for a student.
 
#2. Error Handling:
 
# Add error handling to check if the user inputs valid data types (e.g., integers for marks and age).
 
 
#1. Manage Student List:
 
# Implement a system where users can add and remove students from a list.
 
# Ensure that the list of students can be viewed at any time.
 
#2. Find Passed Students Using List Comprehension:
 
#Use list comprehension to filter out students who have passed based on their marks.
 
# Display the names of all students who scored above 50.
 
#3. Calculate Class Average - Write a function to calculate the average marks of all students in the class.
 
 
#At the end of the week, you should have a fully functional Student Management System with the following features:
 
# Adding new students (name, age, favorite subject, and marks).
 
# Viewing all students and their details.
 
# Calculating and displaying each student’s grade.
 
# Finding students who passed or failed.
 
# Calculating the average marks for a student or the entire class.