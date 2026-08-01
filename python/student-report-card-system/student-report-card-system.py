import time

class Student:
    total_students = 0

    def __init__(self, name, rollno, math, phy, chem):
        self.name = name
        self.rollno = rollno
        self.math = math
        self.phy = phy
        self.chem = chem
        Student.total_students += 1

    @property
    def avg(self):
        return (self.math + self.phy + self.chem) / 3

    @staticmethod
    def grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        return "F"

    @classmethod
    def total_students_count(cls):
        return cls.total_students

    def update_marks(self, subject, marks):
        if not (0 <= marks <= 100):
            print("Invalid marks.")
            return
        if subject == "math":
            self.math = marks
        elif subject == "phy":
            self.phy = marks
        elif subject == "chem":
            self.chem = marks
        else:
            print("Invalid subject.")
            return
        print("Marks updated successfully.")

    def display(self):
        print(f"Name           : {self.name}")
        print(f"Roll No        : {self.rollno}")
        print(f"Maths          : {self.math}")
        print(f"Physics        : {self.phy}")
        print(f"Chemistry      : {self.chem}")
        print(f"Average        : {self.avg:.2f}")
        print(f"Grade          : {Student.grade(self.avg)}")


class SportsStudent(Student):
    def __init__(self, name, rollno, math, phy, chem, sport, coach):
        super().__init__(name, rollno, math, phy, chem)
        self.sport = sport
        self.coach = coach

    def display(self):
        super().display()
        print(f"Sport          : {self.sport}")
        print(f"Coach          : {self.coach}")


students = []

print("=" * 50)
print("        STUDENT MANAGEMENT SYSTEM")
print("=" * 50)
print("\nLoading System...")
time.sleep(1)
print("Preparing Menu...")
time.sleep(1)
print("System Ready!")
time.sleep(0.8)

while True:

    print("\n" + "=" * 50)
    print("         STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Show Topper")
    print("8. Show Rankings")
    print("9. Class Statistics")
    print("10. Save Data to File")
    print("11. Exit")
    print("=" * 50)

    choice = input("Enter your choice: ")

    if choice == "1":
        typ = input("Sports Student? (yes/no): ").lower()
        name = input("Name: ")
        roll = int(input("Roll No: "))
        math = float(input("Maths: "))
        phy = float(input("Physics: "))
        chem = float(input("Chemistry: "))

        if typ == "yes":
            sport = input("Sport: ")
            coach = input("Coach: ")
            s = SportsStudent(name, roll, math, phy, chem, sport, coach)
        else:
            s = Student(name, roll, math, phy, chem)

        students.append(s)
        print("Student added successfully.")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for s in students:
                print("-" * 40)
                s.display()

    elif choice == "3":
        roll = int(input("Enter Roll No: "))
        for s in students:
            if s.rollno == roll:
                s.display()
                break
        else:
            print("Student not found.")

    elif choice == "4":
        roll = int(input("Enter Roll No: "))
        for s in students:
            if s.rollno == roll:
                subject = input("Subject (math/phy/chem): ").lower()
                marks = float(input("New Marks: "))
                s.update_marks(subject, marks)
                break
        else:
            print("Student not found.")

    elif choice == "5":
        roll = int(input("Enter Roll No: "))
        for s in students:
            if s.rollno == roll:
                students.remove(s)
                Student.total_students -= 1
                print("Student deleted.")
                break
        else:
            print("Student not found.")

    elif choice == "6":
        print("Total Students:", Student.total_students_count())

    elif choice == "7":
        if not students:
            print("No students found.")
        else:
            topper = students[0]
            for s in students[1:]:
                if s.avg > topper.avg:
                    topper = s
            print("\nTOPPER")
            print("-" * 30)
            topper.display()

    elif choice == "8":
        if not students:
            print("No students found.")
        else:
            ranked = sorted(students, key=lambda x: x.avg, reverse=True)
            rank = 1
            for s in ranked:
                print("-" * 40)
                print(f"Rank : {rank}")
                s.display()
                rank += 1

    elif choice == "9":
        if not students:
            print("No students found.")
        else:
            total = len(students)
            passed = failed = 0
            total_avg = 0
            high = students[0].avg
            low = students[0].avg

            for s in students:
                total_avg += s.avg
                if s.math >= 35 and s.phy >= 35 and s.chem >= 35:
                    passed += 1
                else:
                    failed += 1

                if s.avg > high:
                    high = s.avg
                if s.avg < low:
                    low = s.avg

            print("\n========== CLASS STATISTICS ==========")
            print(f"Total Students : {total}")
            print(f"Passed Students: {passed}")
            print(f"Failed Students: {failed}")
            print(f"Class Average  : {total_avg/total:.2f}")
            print(f"Highest Average: {high:.2f}")
            print(f"Lowest Average : {low:.2f}")

    elif choice == "10":
        if not students:
            print("No students available to save.")
        else:
            print("Saving student records...")
            time.sleep(1)
            with open("student_data.txt", "w") as file:
                for s in students:
                    if isinstance(s, SportsStudent):
                        file.write(f"sports_student,{s.name},{s.rollno},{s.math},{s.phy},{s.chem},{s.sport},{s.coach}\n")
                    else:
                        file.write(f"student,{s.name},{s.rollno},{s.math},{s.phy},{s.chem}\n")
            print("✓ Student records saved successfully!")
            time.sleep(1)

    elif choice == "11":
        print("\nClosing Student Management System...")
        time.sleep(1)
        print("Thank you for using Student Management System!")
        time.sleep(1)
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")