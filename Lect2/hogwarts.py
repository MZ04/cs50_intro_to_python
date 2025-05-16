#Main purpose: associate each student with the corrispondent house
#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
"""
students={"Hermione": "Gryffindor", "Harry":"Slytherin", "Ron": "Gryffindor", "Draco":"Slytherin"}

for student in students:
    print(student, students[student], sep=", ")"""

#What if we want to associate more than a value to a single key?
students = [
    {"name":"Hermione", "house": "Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house": "Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house": "Gryffindor", "patronus":"Jack Russel Terrier"},
    {"name":"Draco", "house": "Slytherin", "patronus":None}
]

for student in students: 
    print(student["name"], student["house"], student["patronus"], sep=", ")