import csv
from matplotlib import pyplot as plt
import numpy as np
student_dict={}
student_fields = ['student_id', 'name', 'Class_roll_no', 'Batch_name']
student_subject = [student_fields[0], 'bengali','english', 'math', 'physics', 'chemistry']
course_fields = ['course_id', 'course_name']
student_database = 'students.csv'
student_subject_database = 'marks.csv'
course_database='course.csv'


def number_report():
    global student_fields
    global student_subject_database
    global student_database
    global student_subject
    print("--- Creat_report_card ---")
    student_id = input("Enter student_id no. to make report card: ")
    creat_report_card(student_id)
    total_number(student_id)


def total_number(student_id):
    global student_fields
    global student_subject_database
    global student_database
    global student_subject
    with open(student_subject_database, "r", encoding="utf-8") as f:
        csv_data = csv.reader(f)
        count = 0
        for row in csv_data:

            if len(row) > 0:
                if student_id == row[0]:

                    file = open(student_id+".txt", "a")
                    i = 1

                    for i in range(1, 6, 1):
                        y = int(row[i])
                        count = y+count
                    persentage = str(count/5)
        file.write("Your over all persentage is "+persentage+"%"+"\n")
        if ((count/5) <= 40):
            file.write("Sorry You are fail")
        else:    
            file.write("You are pass")


def creat_report_card(student_id):
    global student_fields
    global student_subject_database
    global student_database
    global student_subject
    with open(student_subject_database, "r", encoding="utf-8") as f:
        csv_data = csv.reader(f)
        for row in csv_data:
            if len(row) > 0:
                if student_id == row[0]:
                    file = open(student_id+".txt", "a")
                    file.write("marks"+"     Gread"+" Persentage "+"\n")
                    i = 1
                    for i in range(1, 6, 1):
                        s = "SUBHA"
                        y = int(row[i])
                        if (y >= 90):

                            file.write(
                                row[i]+"          A      "+row[i]+"%"+"\n")
                        elif (y >= 80):
                            file.write(
                                row[i]+"          B      "+row[i]+"%"+"\n")
                        elif (y >= 70):
                            file.write(
                                row[i]+"          C      "+row[i]+"%"+"\n")
                        elif (y >= 60):
                            file.write(
                                row[i]+"          D      "+row[i]+"%"+"\n")
                        elif (y >= 50):
                            file.write(
                                row[i]+"          E      "+row[i]+"%"+"\n")
                        else:

                            file.write(
                                row[i]+"          F      "+row[i]+"%"+"\n")

                    break

        else:
            print("student_id No. not found in our database")
            input("Press any key to continue")
       


''' student_found = False
    updated_data = []
    with open(student_subject_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if student_id != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        '''


def display_menu():
    print("---------------------------------------")
    print(" Student Database Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Add Number")
    print("5. Report Card")
    print("6. Creat Course")
    print("7. histogram")


def add_number():
    print("-------------------------")
    print("Add Student Number")
    print("-------------------------")
    global student_fields
    #global student_database
    global student_subject
    global student_subject_database
    student_id = input("Enter student_id no. to add Number: ")
    student_found = False
    student_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if student_id != row[0]:
                    
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
    
        for field in student_subject:
            value = input("Enter " + field + ":")
            student_data.append(value)
        with open(student_subject_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([student_data])
    else:
        print("student_id No. not found in our database")

    input("Press any key to continue")
        


def delete_student_number():
    global student_fields
    global student_subject_database
    print("--- Delete Student Nummber ---")
    student_id = input("Enter student_id no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_subject_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if student_id != row[0]:
                    
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_subject_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("student_id no marks . ", student_id, "deleted successfully")
    else:
        print("student_id No. not found in our database")

    input("Press any key to continue")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


'''def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")
'''

'''def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    student_id = input("Enter student_id no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if student_id == row[0]:
                    print("----- Student Found -----")
                    print("student_id: ", row[0])
                    print("Name: ", row[1])
                    print("Class_Roll_no: ", row[2])
                    print("Batch name ", row[3])
                    
                    break
        else:
            print("student_id No. not found in our database")
    input("Press any key to continue")
'''


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    student_id = input("Enter student_id no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if student_id == row[0]:
                    index_student = counter
                    print("Student Found: at index ", index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("student_id No. not found in our database")

    input("Press any key to continue")


def creat_course():
    global course_fields
    global student_dict
    print("-------------------------")
    print("Add New Course")
    print("-------------------------")
    
    course_data = []
    student_id=[]
    marks_list=[]
    for field in course_fields:
        value = input("Enter " + field + ":")
        course_data.append(value)
    with open(student_subject_database, "r", encoding="utf-8") as f:
        csv_data = csv.reader(f)
        for line in csv_data:
            if len(line) > 0: 
                marks=input("Enter marks for Student Id- "+line[0]+" ")
                int_marks=int(marks)
                marks_list.append(int_marks)
                student_id.append(line[0])
        for i in range(len(student_id)):
            
            student_dict[student_id[i]]=marks_list[i]
                
                
        
        print(student_dict) 
    resultList = list(student_dict.items())           
    full_list=course_data+resultList
    with open(course_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([full_list])

def histogram():
    a = np.array([22, 87, 5, 43, 56,
              73, 55, 54, 11,
              20, 51, 5, 79, 31,
              27])
 
    # Creating histogram
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(a, bins = [0, 25, 50, 75, 100])
 
# Show plot
    plt.show()    


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    student_id = input("Enter student_id no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if student_id != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("student_id no. ", student_id, "deleted successfully")
    else:
        print("student_id No. not found in our database")

    input("Press any key to continue")


while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()

    elif choice == '2':
        update_student()
    elif choice == '3':
        delete_student()

    elif choice == '4':
        add_number()

    elif choice == '5':
        number_report()
    elif choice == '6':
        creat_course()
    elif choice == '7':
        histogram()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
