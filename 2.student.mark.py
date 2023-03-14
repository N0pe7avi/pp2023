# Create class Course, create object self with id, name and a list marks
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = []
    # Create a method to add mark to the list marks
    def addmark(self, mark):
        self.marks.append(mark)
    
    # Create method to print out the information of the course    
    def __str__(self):
        marks_str = "\n".join(str(mark) for mark in self.marks)
        return f"ID: {self.id}\nName: {self.name}\nMarks:\n{marks_str}"

# Create class Student, create object self with id, name, dob and a list courses   
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = []
    
    # Create a method to add course to the list courses    
    def addcourse(self, course):
        self.courses.append(course)
    
    # Create method to print out the information of the student    
    def __str__(self):
        courses_str = "\n".join(str(course) for course in self.courses)
        return f"ID: {self.id}\nName: {self.name}\nDOB: {self.dob}\nCourses:\n{courses_str}"

# Create class Management to get inputs from user and display information    
class Management:
    # Create lists to store students info and courses info
    def __init__(self):
        self.students = []
        self.courses = []
    
    # Get student info from user and store them in the list students 
    def studentinfo(self):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (dd/mm/yyyy): ")
        student = Student(id, name, dob)
        self.students.append(student)

    # Get course info from user and store them in the list courses 
    def courseinfo(self):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(id, name)
        self.courses.append(course)

    # Get course marks from user based on created course ID, search for the ID in 
    # the created list courses created in class Courses, if the ID is found, get mark
    def coursemarks(self):
        id = input("Enter course ID: ")
        course = next((course for course in self.courses if course.id == id), None)
        if course is None:
            print("Course not found")
        else:
            for student in self.students:
                mark = input(f"Enter {student.name}'s mark for {course.name}: ")
                course.add_mark(mark)

    # Display all information of students and courses
    def display(self):
        print("Students:")
        for student in self.students:
            print(student)
            print()
        print("Courses:")
        for course in self.courses:
            print(course)
            print()

manage = Management()

#Selection menu
while True:
    print("Menu:")
    print("1. Enter student information")
    print("2. Enter course information")
    print("3. Enter course marks")
    print("4. Display all information")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        manage.studentinfo()
    elif choice == "2":
        manage.courseinfo()
    elif choice == "3":
        manage.coursemarks()
    elif choice == "4":
        manage.display()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
