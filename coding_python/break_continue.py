# make a list
students = ["rashmika","jaya","raj","vidhi","rishabh"]

# for loop and inside if loop to break a list

for student in students:
    if student == "raj":
        break;
    print (student)

# same for continuing a list with removing some element

for student in students:
    if student == "vidhi":
         continue;
    print (student)