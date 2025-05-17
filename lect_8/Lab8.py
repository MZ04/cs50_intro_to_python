import sys

class Student: 
    def __init__(self, name, house, patronus):
        if not name: 
            #sys.exit("Missing name")
            raise ValueError("Missing name") #ValueError takes as argument the string to display
        if house not in ["Gryffindor", "HufflePuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
        self.patronus=patronus 
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        print("Expecto patronus")
        match self.patronus:
            case "Stag":
                return "1"
            case "Otter":
                return "2"
            case "Jack Russel Terrier":
                return "3"
            case _:
                return "/"


def main():
    #name, house= get_student()
    student=get_student() #In this case, student is an object of the "Student" class
    print(student)
    #print(student.charm())

#def get_house():
#    return input("House: ")
#
#def get_name():
#    return input("Name: ")


def get_student():
    #student.name=input("Name: ")
    #student.house=input("House: ")
    #Here we defined to fields in the student class: name and house
    return Student(input("Name: ").lstrip(), input("House: ").lstrip(), input("Patronus: ").lstrip()) 
              #input("Name: "), input("House: ") #You aren't return two values, instead one tuple composed by two values
#              [input("Name: "), input("House: ")] if we want to change name or house in the future
#              {"name":input("Name: "), "house":input("House: ")}


if __name__=="__main__":
    main()