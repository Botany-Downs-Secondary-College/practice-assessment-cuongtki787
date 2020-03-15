classSize = 3

names = []
grades = []

for i in range(classSize):
    names = names +[input("Enter student name: ")]
    grades = grades + [input("Enter grade")]

print("Student names: ",names)
print("Student grade: ",grades) 

print("Number of students in this list",len(names))

for i in range(0, len(names)):
    print("Name: ",names[i])
    
print("*********************************")