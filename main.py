#LIBRARY MANAGMENT SYSTEM


from pathlib import Path
import random 
import string
import json

class Library_Management:
    Book_database = "Library.json"
    Book_data = []

    try:
        if Path(Book_database).exists():
            with open(Book_database,"r") as f:
                Book_data = json.loads(f.read())
        else:
            print("NO FILE EXISTS")
                
    except Exception as Err:
        print(f"ERROR OCCURED NAMED-{Err}")

    @classmethod
    def Library_save(cls):
        with open(cls.Book_database,"w") as f:
            f.write(json.dumps(cls.Book_data))



    
    Student_database = "Student.json"
    Student_data = []
    
    try:
        if Path(Student_database).exists():
            with open(Student_database,"r") as s:
                Student_data = json.loads(s.read())
        else:
            print("NO FILE EXISTS")
                
    except Exception as Err:
        print(f"ERROR OCCURED NAMED-{Err}")


    @classmethod
    def Student_save(cls):
        with open(cls.Student_database,"w") as s:
            s.write(json.dumps(cls.Student_data))

    @staticmethod
    def StudentId_Generate(prefix="S"):
        StudentId = ""
        for i in range(5):
            StudentId += random.choice(string.ascii_uppercase + string.digits)

        return prefix+"-"+StudentId

    @staticmethod
    def BookId_Generate(prefix="B"):
        BookId = ""
        for i in range(5):
            BookId += random.choice(string.ascii_uppercase + string.digits)

        return prefix+"-"+BookId


class Admin(Library_Management):
    def Add_Book(self):
        info = {
            "BookName" : input("Enter Book Name:-"),
            "AuthorName" : input("Enter Author Name:-"),
            "Copies" : int(input("How Many Copies")),
            "BookId" : Library_Management.BookId_Generate()
        }

        Library_Management.Book_data.append(info)
        Library_Management.Library_save()

    
    def Update(self):
        try:
            BookName = input("Enter Book Name:-")
            BookId = input("Enter BookId:-")
            Copies = int(input("ENTER COPIES FOR UPDATE:-"))

            BookFound = False
            for i in Library_Management.Book_data:
                if BookName == i["BookName"] and BookId == i["BookId"]:
                    BookFound =True
                    i["Copies"] += Copies

            if BookFound == False:
                return "No Such Book Found"

            Library_Management.Library_save()

        except Exception as Err:
            print(f"ERROR OCCURED NAMED:-{Err}")

    def Book_Info(self):
        try:
            BookName = input("Enter Book Name To See:-")
            BookId = input("Enter Book ID:-")
            BookFound = False
            for i in Library_Management.Book_data:
                if BookName == i["BookName"] and BookId == i["BookId"]:
                    print(i)
                    BookFound = True
                    break
            if BookFound == False:
                print(f"NO BOOK FOUND IN DATA{BookName}")

        except Exception as Err:
            print(f"ERROR OCCURED NAMED:-{Err}")



    def Show_All(self):
        try:
            if len(Library_Management.Book_data) > 0:
                print(Library_Management.Book_data)
            else:
                print("NO BOOKS AVAILAIBLE")

        except Exception as Err:
            print (F"ERROR OCCURED NAMED:-{Err}")


    def Delete_Book(self):
        try:
            BookName = input("Enter Book Name:-")
            BookId = input("Enter BookID:-")

            BookFound = False
            for i in Library_Management.Book_data: 
                if BookName == i["BookName"] and BookId == i["BookId"]:
                    Library_Management.Book_data.remove(i)
                    BookFound = True
                    
            if BookFound == False:
                return "No Book found"

            Library_Management.Library_save()

        except Exception as Err:
            print(f"ERROR OCCURED NAMED:-{Err}")



class Student(Library_Management):
    def Enrollment_Form(self):
        info ={
            "Name" : input("Enter Your Name"),
            "Age" : int(input("Enter Your Age")),
            "Email" : input("Enter Your Email"),
            "StudentId" : Library_Management.StudentId_Generate(),
            "IssuedBook" : []
        }

        Library_Management.Student_data.append(info)
        Library_Management.Student_save()

        print(f"STUDENT ENROLLED SUCESSFULLY\n YOUR STUDENT ID: {info['StudentId']}")


    def IssueBook(self):
        BookName = input("Enter Book Name:-")
        BookId = input("Enter Book ID:-")
        StudentId = input("Enter Student ID:-")


        BookFound = None
        StudentFound = None
        
        for i in Library_Management.Book_data:
            if BookName == i["BookName"] and i["Copies"] > 0  and BookId == i["BookId"]:
                BookFound = i
                break
        if BookFound is None:
            return "No Book Found"

        
        for j in Library_Management.Student_data:
            if j["StudentId"] == StudentId:
                StudentFound = j
                break
        if StudentFound is None:
            return "No Student Found"

        
        if BookFound and StudentFound:
            BookFound["Copies"] -= 1
            StudentFound["IssuedBook"].append(BookName)
            
            Library_Management.Library_save()
            Library_Management.Student_save()



    def ReturnBook(self):
        BookName = input("Enter Book Name:-")
        BookId = input("Enter Book ID:-")
        StudentId = input("Enter StudentID:-")

        BookFound = None
        StudentFound = None

        for i in Library_Management.Student_data:
            if i["StudentId"] == StudentId and BookName in i["IssuedBook"]:
                StudentFound = i
                break
        if StudentFound is None:
            return "No Student Found"

        for j in Library_Management.Book_data:
            if j["BookName"] == BookName and j["BookId"] == BookId:
                BookFound = j
                break
        if BookFound is None:
            return "No Book Record Found"

        if BookFound and StudentFound:
            BookFound["Copies"] += 1
            StudentFound["IssuedBook"].remove(BookName)

            Library_Management.Library_save()
            Library_Management.Student_save()
            

    def AvailableBook(self):
        if len(Library_Management.Book_data) > 0:
            for i in Library_Management.Book_data:
                print(f"BOOK NAME : {i['BookName']}")
                print(f"AUTHOR NAME : {i['AuthorName']}")
                print(f"BOOK ID : {i['BookId']}")
                print(f"TOTAL COPIES : {i['Copies']}")
                print("-"*20)
        else:
            print("NO BOOK AVAILABLE")


    def BookDetails(self):
        BookId = input("Enter Book Id")

        BookFound = False
        for i in Library_Management.Book_data:
            if BookId == i["BookId"]:
                BookFound =True
                print(f"BOOK NAME : {i['BookName']}")
                print(f"AUTHOR NAME : {i['AuthorName']}")
                print(f"TOTAL COPIES : {i['Copies']}")

        if BookFound == False:
            print("NO BOOK FOUND")




admin_object = Admin()
student_object = Student()

print("WHO ARE YOU ?")
print("1. ADMIN")
print("2. STUDENT")
User = int(input("TELL THE SYSTEM:-"))

Admin_Password = 123
if User == 1:
    password = int(input("ENTER ADMIN PASSWORD:-"))
    if password == Admin_Password:
        while True:
            print("\n" + "="*40)
            print("! YOUR ADMIN MENU IS HERE !")
            print("PRESS 1 To Store Book")
            print("PRESS 2 To Make Update")
            print("PRESS 3 To See Book Information")
            print("PRESS 4 To See All Books")
            print("PRESS 5 To Remove Book")
            print("PRESS 0 TO EXIT")
            print("="*40)

            Tell = int(input("TELL WHAT YOU WANT TO DO:-"))
            if Tell == 1:
                admin_object.Add_Book()

            elif Tell == 2:
                admin_object.Update()

            elif Tell == 3:
                admin_object.Book_Info()

            elif Tell == 4:
                admin_object.Show_All()

            elif Tell == 5:
                admin_object.Delete_Book()

            elif Tell ==0:
                break
    else:
        print("Wrong Password")

elif User == 2:
    while True:
        print("\n" + "="*40)
        print("! YOUR MENUE IS HERE !")
        print("PRESS 1 To Enroll As Student")
        print("PRESS 2 To Issue Book")
        print("PRESS 3 For Return Book")
        print("PRESS 4 To Check Available Books")
        print("PRESS 5 To Check Book Details")
        print("PRESS 0 TO EXIT")
        print("="*40)

        Tell = int(input("TELL WHAT YOU WANT TO DO:-"))

        if Tell == 1:
            student_object.Enrollment_Form()

        elif Tell == 2:
            student_object.IssueBook()

        elif Tell == 3:
            student_object.ReturnBook()

        elif Tell == 4:
            student_object.AvailableBook()

        elif Tell == 5:
            student_object.BookDetails()
        elif Tell == 0:
             break
