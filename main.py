class Student:
    def __init__(self,Roll_no,Name,Age):
        self.Roll_no=Roll_no
        self.Name=Name
        self.Age=Age
  
    def Display(self):
        print("Student Name: ",self.Name)
        print("Student Roll Number: ",self.Roll_no)
        print("Age: ",self.Age)

class School:
    def __init__(self):
        self.students={}

    def Add(self):
        roll=input("Enter the Roll Number:")

        if roll in self.students:
            print("Student already Exsists!")
            return

        Name=input("Enter the Name:")
        Age=int(input("Enter the Age:"))
        
        student=Student(roll,Name,Age)
        self.students[roll]=student
        print("Student Added Successfully!")

    def Update(self):
        roll=input("Enter the Roll Number:")
        student=self.students.get(roll)

        if student:
            student.Name=input("Enter the new Name:")
            student.Age=int(input("Enter the new Age:"))
            print("Student Updated Successfully!") 
        else:
            print("Student Not Found!")

    def delete(self):
        roll=input("Enter the Roll Number:")

        if roll in self.students:
            del self.students[roll]
            print("Student Deleted!")
        else:
            print("Student Not Found!")

    def display_all(self):
        if len(self.students)==0:
            print("No student!") 
        else:
            print("----------------------Students List----------------------")         
            for student in self.students.values():
                student.Display()
                print("---------------------------------------------------------")    

    def Menu(self):
        while True:
            print("================Students Management System================")
            print("1.Add Student")
            print("2.Update Student")
            print("3.Delete Student")
            print("4.Display Students")
            print("5.Exit")
            print("==========================================================") 

            choice=int(input("Enter your choice:"))
            if choice ==1:
                self.Add()
            elif choice==2:
                self.Update()     
            elif choice==3:
                self.delete()
            elif choice==4:
                self.display_all()
            elif choice==5:
                print("Thank You!")
                break
            else:
                print("Invalid Choice!")

s1=School()
s1.Menu()                                                                            