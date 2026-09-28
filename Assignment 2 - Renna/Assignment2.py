# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Brennan Renna
# Assignment Number: Assignment 2
# Due Date: 10/02/2026
# Purpose: This program reads student names and six scores from an input file,
# calculates each student's final average, and displays the students in
# descending order based on their final average.
# Resources Used: Assignment 2 instructions and course materials.

#function to determine the average of the students grades
def get_average(student):
    return student[1]

#Opens and reads the input file to access student grades
input_file = open("Assignment2input.txt", "r")

students = []

#Reads each line in the input file to get each name and scores of the students
for line in input_file:
    data = line.split()

    name = data [0]

    score1= float(data[1])
    score2 = float(data[2])
    score3 = float(data[3])
    score4 = float(data[4])
    score5 = float(data[5])
    score6 = float(data[6])
    average = (score1 + score2 + score3 + score4 + score5 + score6) / 6
#Adds the student's name and now average score to the list
    students.append((name, average))

input_file.close()

#Sorts students from highest avr score to lowest avr score
students.sort(key=get_average, reverse=True)

#Displays the student's name and average and formats it to the 2nd decimal place
for student in students:
    print(student[0], format(student[1], ".2f"))
