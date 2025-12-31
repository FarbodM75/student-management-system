# The starting point of my course project
from datetime import date
def ask_date():
    while True:
        d = input("Enter date (YYYY-MM-DD): ").strip()
        if len(d) != 10 or d[4] != '-' or d[7] != '-':
            print("Invalid date format! Use YYYY-MM-DD.")
            continue
        #if input was not a number
        y, m, day = d[:4], d[5:7], d[8:]
        if not (y.isdigit() and m.isdigit() and day.isdigit()):
            print("Invalid date! Only numbers allowed.")
            continue
        # if month is more than 12
        y, m, day = int(y), int(m), int(day)
        if not (1 <= m <= 12):
            print("Invalid month! Try again.")
            continue
        # if input day is out of range
        mdays = [31, 28 + ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not (1 <= day <= mdays[m-1]):
            print("Invalid day for that month! Try again.")
            continue
        today = date.today()
        input_date = date(y, m, day)
        # if input is in the future
        if input_date > today:
            print("Input date is later than today. Try again!")
            continue
        if (today - input_date).days > 30:
            print("Input date is older than 30 days. Contact opinto.")
            return

        return input_date



#function menu
def show_menu():
    print("Select one of the following:")
    print("1) Add student ")
    print("2) Search student ")
    print("3) Search course ")
    print("4) Add course completion ")
    print("5) Show student's record ")
    print("0) Exit ")
    choice = input("Enter your choice (0-5): \n")
    return choice



# function Add student
def add_student():
    #The starting year
    from datetime import datetime
    student_time = datetime.today()
    starting_year = student_time.strftime("%Y")

    #First, middle and last name
    student_first_name = input("Enter the student's first name: \n")
    while not student_first_name.isalpha() or not student_first_name.istitle():
        print("Incorrect! Make sure it starts with a capital letter and only contains letters.")
        student_first_name = input("Enter the student's first name again: \n")

    student_last_name = input("Enter the student's last name: \n")
    while not student_last_name.isalpha() or not student_last_name.istitle():
        print("Incorrect! Make sure it starts with a capital letter and only contains letters.")
        student_last_name = input("Enter the student's last name again: \n")
        
    student_middle_name = input("Enter the student's middle name (if not applicable press ENTER): \n")
    if student_middle_name:
        while student_middle_name != "" and (not student_middle_name.isalpha() or not student_middle_name.istitle()):
            print("Incorrect! Make sure it starts with a capital letter and only contains letters.")
            student_middle_name = input("Enter the student's middle name again (if not applicable press ENTER): \n")
    #Email   
    student_email = (student_first_name + "." + student_last_name + "@lut.fi")
    #ID
    file = open('students.txt', 'r')
    stud_list = file.readlines()
    file.close()
    
    import random
    all_ids = []
    for line in stud_list:
        student_data = line.strip().split(",")
        #The values:
        stud_id, last, first, middle, email, year, program = student_data
        all_ids.append(stud_id)
            
    while True:
        new_stud_id = str(random.randint(10000, 99999))
        if new_stud_id not in all_ids:  #checks if this ID is unique or not
            break
    student_id = new_stud_id

    
    #Program
    bachelor_program = input("Select student's bachelor program: \n"
                             "* CE: Computational Engineering\n"
                             "* EE: Electrical Engineering\n"
                             "* ET: Energy Technology\n"
                             "* ME: Mechanical Engineering\n"
                             "* SE: Software Engineering\n").upper()
    while bachelor_program not in ["CE", "EE", "ET", "ME", "SE"]:
        print("Invalid selection! Please select from the given options only.")
        bachelor_program = input("Select student's bachelor program again: \n"
                             "* CE: Computational Engineering\n"
                             "* EE: Electrical Engineering\n"
                             "* ET: Energy Technology\n"
                             "* ME: Mechanical Engineering\n"
                             "* SE: Software Engineering\n").upper()
        
    logged_student = (str(student_id) + "," + student_last_name + "," + student_first_name + "," + student_middle_name + "," + student_email + "," + starting_year + "," + bachelor_program )
    file = open('students.txt', 'a')
    file.write(f"{logged_student}\n")
    file.close()
    print("Student has been added successfully!")



# function search student
def search_student():
    stud_name = input("Give at least 3 characters of the student's first, middle or last name: \n")
    while len(stud_name) < 3 or not stud_name.replace(" ", "").isalpha():
        print("Error! Please Enter at least 3 characters and only characters.")
        stud_name = input("Give at least 3 characters of the student's first, middle or last name again: ").capitalize().strip()
        
    file = open('students.txt', 'r')
    stud_list = file.readlines()
    found = False
    
    for line in stud_list:
        student_data = line.strip().split(",")
        #The values:
        student_id, last, first, middle, email, year, program = student_data
            
        if (stud_name in first) or (stud_name in middle) or (stud_name in last):
            print("Matching students:")
            print(f"ID: {student_id}, {last}, {first}")
            found = True
                
    if found == False: # if it was still false and didn't change to true(found), print next line.
        print("No available student!")
                
    file.close()



  # function search course          
def search_course():
    cour_name = input("Give at least 3 characters of the name of the course or the teacher: \n")
    while len(cour_name) < 3 or not cour_name.replace(" ", "").isalpha():
        print("Error! Please Enter at least 3 characters and only characters.")
        cour_name = input("Give at least 3 characters of the name of the course or the teacher: \n")
        
    file = open('courses.txt', 'r')
    cour_list = file.readlines()
    found = False
    
    for line in cour_list:
        course_data = line.strip().split(",")
        #The values2:
        course_id, course_name, course_credit, *teachers = course_data 
        if (cour_name.lower() in course_name.lower()):
            teacher_str = str(teachers).replace("[", "").replace("]", "").replace("'", "")
            print(f"ID: {course_id}, Name: {course_name}, Teacher(s): {teacher_str}")
            found = True
        else:
            for t in teachers:
                if cour_name.lower() in t.lower():
                    teacher_str = str(teachers).replace("[", "").replace("]", "").replace("'", "")
                    print(f"ID: {course_id}, Name: {course_name}, Teacher(s): {teacher_str}")
                    found = True
                    break 
    if found == False:
        print("No available Courses or teachers!")

    file.close()



# function add course completion
def course_completion():
    #For finding course id
    file = open('courses.txt', 'r')
    course_list = file.readlines()
    file.close()

    found_course = False
    while not found_course:
        cour_id = input("Enter course ID: \n")
        for line in course_list:
            course_data = line.strip().split(",")
            #The values1:
            course_id, course_name, course_credit, *teachers = course_data
            if (cour_id == course_id):
                found_course = True
                break
                
        if not found_course:
            print("Not found! Enter the correct course ID: \n")
    
    #for finding student id
    file = open('students.txt', 'r')
    stud_list = file.readlines()
    file.close()
    
    found_student = False
    while not found_student:
        stud_id = input("Enter student ID: \n")
        for line2 in stud_list:
            student_data = line2.strip().split(",")
            #The values2:
            student_id, last, first, middle, email, year, program = student_data
            if (stud_id == student_id):
                found_student = True
                break
        if not found_student:
            stud_id = input("Enter student ID again: \n")
    
    #for grade
    grad = input("Give the grade: \n")
    while grad not in ["1", "2", "3", "4", "5"]:
        print("Error! Grade is not a correct grade. ")
        grad = input("Give the grade: \n")
    # for date
    input_date = ask_date()
    if not input_date:
        return
    
    # Read it then close it
    file = open('passed.txt', 'r')
    passed_list = file.readlines()
    file.close()

    updated = False
    new_passed_list = [] 

    for line3 in passed_list:
        passed_data = line3.strip().split(",")
        course_passed_id, student_passed_id, completion_date, passed_grade = passed_data

        if stud_id == student_passed_id and cour_id == course_passed_id: 
            if int(grad) > int(passed_grade): # If it needs to be updated
                new_passed_list.append(f"{cour_id},{stud_id},{input_date.isoformat()},{grad}\n")
                print(f"Updated grade from {passed_grade} to {grad}.")
            else: # If no update is needed, Keep the old record
                new_passed_list.append(line3)
                print(f"No update. Previous grade ({passed_grade}) is higher or equal.")
            updated = True
        else:
            new_passed_list.append(line3) #adds everything from the passed_list to a new list

    if not updated:
        # add the new entry
        new_passed_list.append(f"{cour_id},{stud_id},{input_date.isoformat()},{grad}\n")
        print("Record added!")

    # Write everything back to the file
    file = open('passed.txt', 'w')
    file.writelines(new_passed_list)
    file.close()
   

# function student record                     
def show_student_record():
    #for finding student id
    file = open('students.txt', 'r')
    stud_list = file.readlines()
    file.close()
    
    found_student = False
    while not found_student:
        stud_id = input("Enter student ID: \n")
        for line in stud_list:
            student_data = line.strip().split(",")
            #The values1:
            student_id, last, first, middle, email, year, program = student_data
            if (stud_id == student_id):
                found_student = True
                print(  f"Student ID: {student_id} \n"
                        f"Name: {last}, {first} \n"
                        f"Starting year: {year} \n"
                        f"Major: {program} \n"
                        f"Email: {email} \n\n"

                        f"Passed Courses: \n")
                
                # Read passed records and courses
                file = open('passed.txt', 'r')
                passed_list = file.readlines()
                file.close()

                file = open('courses.txt', 'r')
                course_list = file.readlines()
                file.close()
                
                for line2 in passed_list:
                    passed_data = line2.strip().split(",")
                    #The_values3:
                    course_passed_id, student_passed_id, completion_date, passed_grade = passed_data
                          
                    if stud_id == student_passed_id:
                        for line3 in course_list:
                            course_data = line3.strip().split(",")
                            #The values1:
                            course_id, course_name, course_credit, *teachers = course_data
                            teacher_str = str(teachers).replace("[", "").replace("]", "").replace("'", "")
                          
                            if (course_passed_id == course_id):
                                print(f"Course ID: {course_id}, Name: {course_name}, Credits: {course_credit} \n"
                                    f"Date: {completion_date}, Teacher(s): {teacher_str}, Grade: {passed_grade}\n")
                
                break #exits the for loop after finding everything
            
        if not found_student:
            print("Student not found!")
            return
    



def main():
    while True:
        choice = show_menu()
        if choice == "1":
            add_student()   
        elif choice == "2":
            search_student()
        elif choice == "3":
            search_course()
        elif choice == "4":
            course_completion()
        elif choice == "5":
            show_student_record()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
