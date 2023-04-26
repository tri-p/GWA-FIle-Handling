# PABUNA, KATRINA B. 
# Write a Python program that read a file containing the name of 20 students together with their GWA
# The program will output the name of the student who got the highest GWA (including the GWA)

# Open students_gwa.txt (read)
with open("students_gwa.txt") as input_students_gwa:
    # Set the lowest possible GWA a student can have and set a GWA that is invalid
    highest_gwa = 5.00
    lowest_gwa = 0.99
    highest_student = ""
    highest_student_gwa = ""
    # Read the inputs for students and GWA line by line and split the name and their GWA
    for line in input_students_gwa:
        student, gwa_str = line.strip().split(": ")
        # If the GWA < lowest possible GWA and > invalid GWA, get highest GWA and name
        # If there is more than one student who got the highest GWA, record it as well


# Print the output