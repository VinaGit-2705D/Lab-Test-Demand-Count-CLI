import json
from datetime import datetime

FILE = "test_requests.json"

test_requests = []


# ---------------- FILE STORAGE ----------------

def load_data():
    global test_requests

    try:
        with open(FILE, "r") as file:
            test_requests = json.load(file)

    except:
        test_requests = []


def save_data():
    with open(FILE, "w") as file:
        json.dump(test_requests, file, indent=4)



# ---------------- LOGIN ----------------

def login():

    username = "admin"
    password = "1234"

    print("\n===== HEMAS HOSPITAL LAB LOGIN =====")

    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Login Successful")
        return True

    else:
        print("Invalid Login")
        return False



# ---------------- VALIDATIONS ----------------

def get_name():

    while True:
        name = input("Enter Patient Name: ")

        if name.strip() != "":
            return name

        print("Name cannot be empty")



def get_age():

    while True:
        age = input("Enter Age: ")

        if age.isdigit():
            return age

        print("Enter valid age")



def get_phone():

    while True:
        phone = input("Enter Phone Number: ")

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Enter 10 digit phone number")



def get_doctor():

    while True:
        doctor = input("Enter Doctor Name: ")

        if doctor.strip() != "":
            return doctor

        print("Doctor name required")



def get_date():

    while True:

        date = input("Enter Date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except:
            print("Invalid Date Format")



# ---------------- PATIENT ID ----------------

def generate_patient_id():

    if len(test_requests) == 0:
        return 1001

    return test_requests[-1]["Patient ID"] + 1




# ---------------- ADD REQUEST ----------------

def add_request():

    print("\n--- ADD TEST REQUEST ---")

    patient_id = generate_patient_id()

    print("Patient ID:", patient_id)


    name = get_name()
    age = get_age()
    phone = get_phone()
    doctor = get_doctor()


    print("\nAvailable Tests")
    print("1. Blood Test")
    print("2. X-Ray")
    print("3. MRI Scan")
    print("4. CT Scan")
    print("5. Urine Test")


    tests = {
        "1":"Blood Test",
        "2":"X-Ray",
        "3":"MRI Scan",
        "4":"CT Scan",
        "5":"Urine Test"
    }


    choice = input("Select Test: ")


    if choice not in tests:
        print("Invalid Test")
        return


    test = tests[choice]

    date = get_date()



    for r in test_requests:

        if r["Name"] == name and r["Test"] == test and r["Date"] == date:
            print("Duplicate Request Found")
            return



    request = {

        "Patient ID": patient_id,
        "Name": name,
        "Age": age,
        "Phone": phone,
        "Doctor": doctor,
        "Test": test,
        "Date": date

    }


    test_requests.append(request)

    save_data()

    print("Request Added Successfully")





# ---------------- VIEW ----------------

def view_all():

    print("\n--- ALL REQUESTS ---")


    if len(test_requests)==0:
        print("No Data")
        return


    for i,r in enumerate(test_requests,start=1):

        print("\nRequest No:",i)

        for key,value in r.items():
            print(key,":",value)




# ---------------- DEMAND REPORT ----------------

def demand_report():

    count={}


    for r in test_requests:

        test=r["Test"]

        count[test]=count.get(test,0)+1



    print("\n===== LAB REPORT =====")


    for test,total in count.items():

        print(test,":",total)



    if count:

        popular=max(count,key=count.get)

        print("Most Requested:",popular)




# ---------------- SEARCH TEST ----------------

def search_test():

    name=input("Enter Test Name: ")

    found=False


    for r in test_requests:

        if r["Test"].lower()==name.lower():

            print(r)

            found=True



    if not found:
        print("Not Found")




# ---------------- SEARCH ID ----------------

def search_id():

    try:

        pid=int(input("Enter Patient ID: "))


        for r in test_requests:

            if r["Patient ID"]==pid:

                print(r)
                return


        print("Patient Not Found")


    except:

        print("Enter number only")





# ---------------- UPDATE ----------------

def update_request():

    try:

        pid=int(input("Enter Patient ID: "))


        for r in test_requests:


            if r["Patient ID"]==pid:


                r["Phone"]=get_phone()

                r["Doctor"]=get_doctor()

                r["Date"]=get_date()


                save_data()

                print("Updated Successfully")

                return



        print("Patient Not Found")


    except:

        print("Invalid ID")





# ---------------- DELETE ----------------

def delete_request():

    try:

        pid=int(input("Enter Patient ID: "))


        for r in test_requests:

            if r["Patient ID"]==pid:

                test_requests.remove(r)

                save_data()

                print("Deleted Successfully")

                return


        print("Not Found")


    except:

        print("Invalid Input")





# ---------------- MAIN ----------------


load_data()


if login():


    while True:


        print("\n========== HEMAS HOSPITAL LAB ==========")

        print("1. Add Test Request")
        print("2. View All Requests")
        print("3. Demand Report")
        print("4. Search Test")
        print("5. Search Patient ID")
        print("6. Update Request")
        print("7. Delete Request")
        print("8. Exit")


        choice=input("Enter Choice: ")



        if choice=="1":
            add_request()

        elif choice=="2":
            view_all()

        elif choice=="3":
            demand_report()

        elif choice=="4":
            search_test()

        elif choice=="5":
            search_id()

        elif choice=="6":
            update_request()

        elif choice=="7":
            delete_request()

        elif choice=="8":
            print("Thank You")
            break

        else:
            print("Invalid Choice")