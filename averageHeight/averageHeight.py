# This will calculate the average heights in a list
# Author: Ray Bolin
# Date: 1/3/2022
# 100DaysOfCoding

student_heights = input("Input a list of student heights:  ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

num_heights = 0
total = 0
for height in student_heights:
    total += height
    num_heights += 1

avg = round(total / num_heights)
print(avg)
