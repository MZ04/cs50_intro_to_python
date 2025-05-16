import csv

#students=[]
#
#with open("students.csv") as file:
#    for line in file:
#        #We know that split() returns a list, but since we know that the list is going to be 
#        # formed by two elements, we can "unpack" it in name and house 
#        name, house = line.rstrip().split(",")
#        students.append(f"{name} is in {house}")

##for student in sorted(students):
##    print(student)
#
#students=[]
#
#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(",")
#        student={"name":name, "house":house}
#        students.append(student)
#
##Definition of the function which we base our sort on
##This function defines the variable to consider for the sort
#def get_name(student):
#    return student['name']
#
#def get_house(student):
#    return student['house']
#
##for student in sorted(students, key=get_name, reverse=True):
#for student in sorted(students, key=lambda student:student['name']):
##The lambda function defined is equal to the get_name function
##The syntax of a lambda function is similar to the one in ML
#    #To refer to the values in the dictionary inside a print, we use single quotes otherwise it i going to 
#    # conflict with the double quotes of the string
#    print(f"{student['name']} is in {student['house']}")
#students = []
#
#with open("students.csv") as file:
##    for line in file:
##        #name, home=line.rstrip.split(",") -> Generates an error, since considering "Harry, Number Four, Privet drive" we have more than a comma 
##        student={"name":name, "home":home}
##        students.append(student)
#    reader=csv.reader(file)
#    for name, home in reader:
#        students.append({"name": name, "home": home})
#
#for student in sorted(students, key=lambda student: student['name']):
#    print(f"{student['name']} lives in {student['home']}")

name =input("What's your name? ")
home=input("Where's your home? ")

with open("students.csv", "a") as file:
    writer=csv.DictWriter(file, fieldnames=["name", "home"])
    #The fieldNames is useful to define the order in which represent the data in the csv file
    #We know, in fact, that when we read it the program doesn't know directly which value is associated to which one
    writer.writerow({"home":home, "name":name})