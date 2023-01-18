# Use a for loop to calculate the average height of a group of students.
student_heights = input("Input a list a student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
               

#print(student_heights)

num_of_students = 0

height_total = 0

for height in student_heights:
    height_total += height
    num_of_students += 1
    
    
average_height = round(height_total/num_of_students)

print(f"The average height is {average_height}cm")