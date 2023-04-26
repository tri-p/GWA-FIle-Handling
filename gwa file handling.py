# PABUNA, KATRINA B. 
# Write a Python program that read a file containing the name of 20 students together with their GWA
# The program will output the name of the student who got the highest GWA (including the GWA)

# Open students_gwa.txt (read)
with open("students_gwa.txt") as input_students_gwa:
    # Read the inputs for students and GWA line by line and split the name and their GWA
    for line in input_students_gwa:
        student, gwa_str = line.strip().split(": ")



# Print the output