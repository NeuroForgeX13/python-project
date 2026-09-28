# ==========================================
# HOSPITAL MANAGEMENT SYSTEM
# BASIC PYTHON PROJECT
# PART 1
# ==========================================


patients = []

doctors = []

appointments = []

medicines = []

bills = []



# ==========================================
# ADD PATIENT
# ==========================================

def add_patient():

    print("\n===== ADD PATIENT =====")


    name = input("Enter Patient Name: ")

    age = input("Enter Patient Age: ")

    gender = input("Enter Gender: ")



    print("\nSelect Disease")

    print("1. Covid")

    print("2. Skin Problem")

    print("3. Cancer")

    print("4. Other")



    choice = input("Enter Choice: ")



    if choice == "1":

        disease = "Covid"


    elif choice == "2":

        disease = "Skin Problem"


    elif choice == "3":

        disease = "Cancer"


    else:

        disease = input("Enter Disease Name: ")



    patient = {

        "id": len(patients)+1,

        "name": name,

        "age": age,

        "gender": gender,

        "disease": disease

    }



    patients.append(patient)



    print("Patient Added Successfully!")





# ==========================================
# SHOW PATIENT
# ==========================================

def show_patient():


    print("\n===== PATIENT RECORD =====")



    for p in patients:


        print("----------------------")

        print("Patient ID:",p["id"])

        print("Name:",p["name"])

        print("Age:",p["age"])

        print("Gender:",p["gender"])

        print("Disease:",p["disease"])







# ==========================================
# ADD DOCTOR
# ==========================================


def add_doctor():

    print("\n===== ADD DOCTOR =====")


    name = input("Doctor Name: ")


    specialization = input("Specialization: ")


    fee = int(input("Doctor Fee: "))



    doctor = {


        "id":len(doctors)+1,

        "name":name,

        "specialization":specialization,

        "fee":fee

    }



    doctors.append(doctor)



    print("Doctor Added Successfully!")






# ==========================================
# SHOW DOCTOR
# ==========================================


def show_doctor():


    print("\n===== DOCTOR RECORD =====")



    for d in doctors:


        print("----------------------")

        print("Doctor ID:",d["id"])

        print("Name:",d["name"])

        print("Specialization:",d["specialization"])

        print("Fee:",d["fee"])








# ==========================================
# APPOINTMENT SYSTEM
# ==========================================


def appointment():


    print("\n===== APPOINTMENT =====")


    patient_id=int(input("Enter Patient ID: "))


    doctor_id=int(input("Enter Doctor ID: "))



    time=input("Enter Appointment Time: ")



    appointment={


        "patient_id":patient_id,

        "doctor_id":doctor_id,

        "time":time

    }



    appointments.append(appointment)



    print("Appointment Booked!")







# ==========================================
# SHOW APPOINTMENT
# ==========================================


def show_appointment():


    print("\n===== APPOINTMENTS =====")



    for a in appointments:


        print("----------------------")

        print("Patient ID:",a["patient_id"])

        print("Doctor ID:",a["doctor_id"])

        print("Time:",a["time"])







# ==========================================
# MAIN MENU
# ==========================================


while True:


    print("\n========== HOSPITAL MENU ==========")


    print("1. Add Patient")

    print("2. Show Patient")

    print("3. Add Doctor")

    print("4. Show Doctor")

    print("5. Book Appointment")

    print("6. Show Appointment")

    print("7. Exit")



    choice=input("Enter Choice: ")




    if choice=="1":

        add_patient()



    elif choice=="2":

        show_patient()



    elif choice=="3":

        add_doctor()



    elif choice=="4":

        show_doctor()



    elif choice=="5":

        appointment()



    elif choice=="6":

        show_appointment()



    elif choice=="7":

        print("Thank You")

        break



    else:

        print("Wrong Choice")

        

# ==========================================
# HOSPITAL MANAGEMENT SYSTEM
# PART 2
# MEDICINE + BILL + FINAL SLIP
# ==========================================






# ==========================================
# ADD MEDICINE
# ==========================================

def add_medicine():


    print("\n===== ADD MEDICINE =====")



    patient_id = int(input("Enter Patient ID: "))


    doctor_id = int(input("Enter Doctor ID: "))



    medicine_name = input("Enter Medicine Name: ")


    medicine_price = int(input("Enter Medicine Price: "))



    medicine = {


        "patient_id": patient_id,

        "doctor_id": doctor_id,

        "medicine": medicine_name,

        "price": medicine_price

    }



    medicines.append(medicine)



    print("Medicine Added Successfully!")







# ==========================================
# SHOW MEDICINE
# ==========================================


def show_medicine():


    print("\n===== MEDICINE RECORD =====")



    for m in medicines:


        print("----------------------")

        print("Patient ID:",m["patient_id"])

        print("Doctor ID:",m["doctor_id"])

        print("Medicine:",m["medicine"])

        print("Price:",m["price"])








# ==========================================
# CREATE BILL
# ==========================================


def create_bill():


    print("\n===== CREATE BILL =====")



    patient_id = int(input("Enter Patient ID: "))



    doctor_fee = int(input("Enter Doctor Fee: "))



    medicine_fee = int(input("Enter Medicine Fee: "))



    test_fee = int(input("Enter Test Fee: "))



    total = doctor_fee + medicine_fee + test_fee



    bill = {


        "patient_id":patient_id,

        "doctor_fee":doctor_fee,

        "medicine_fee":medicine_fee,

        "test_fee":test_fee,

        "total":total

    }



    bills.append(bill)



    print("Bill Created Successfully!")







# ==========================================
# SHOW BILL
# ==========================================


def show_bill():


    print("\n===== BILL DETAILS =====")



    for b in bills:


        print("----------------------")

        print("Patient ID:",b["patient_id"])

        print("Doctor Fee:",b["doctor_fee"])

        print("Medicine Fee:",b["medicine_fee"])

        print("Test Fee:",b["test_fee"])

        print("Total Bill:",b["total"])








# ==========================================
# FINAL PATIENT SLIP
# ==========================================


def final_slip():


    print("\n========== HOSPITAL SLIP ==========")



    patient_id=int(input("Enter Patient ID: "))



    print("\n--- Patient Detail ---")



    for p in patients:


        if p["id"] == patient_id:


            print("Name:",p["name"])

            print("Age:",p["age"])

            print("Gender:",p["gender"])

            print("Disease:",p["disease"])





    print("\n--- Doctor Detail ---")



    for a in appointments:


        if a["patient_id"] == patient_id:


            for d in doctors:


                if d["id"] == a["doctor_id"]:


                    print("Doctor:",d["name"])

                    print("Specialization:",d["specialization"])

                    print("Appointment Time:",a["time"])







    print("\n--- Medicine Detail ---")



    for m in medicines:


        if m["patient_id"] == patient_id:


            print("Medicine:",m["medicine"])

            print("Medicine Price:",m["price"])






    print("\n--- Bill Detail ---")



    for b in bills:


        if b["patient_id"] == patient_id:


            print("Doctor Fee:",b["doctor_fee"])

            print("Medicine Fee:",b["medicine_fee"])

            print("Test Fee:",b["test_fee"])

            print("Total Bill:",b["total"])




    print("\n========== THANK YOU ==========")



# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n========== HOSPITAL MENU ==========")

    print("1. Add Patient")
    print("2. Show Patient")
    print("3. Add Doctor")
    print("4. Show Doctor")
    print("5. Book Appointment")
    print("6. Show Appointment")
    print("7. Add Medicine")
    print("8. Show Medicine")
    print("9. Create Bill")
    print("10. Show Bill")
    print("11. Final Slip")
    print("12. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        show_patient()

    elif choice == "3":
        add_doctor()

    elif choice == "4":
        show_doctor()

    elif choice == "5":
        appointment()

    elif choice == "6":
        show_appointment()

    elif choice == "7":
        add_medicine()

    elif choice == "8":
        show_medicine()

    elif choice == "9":
        create_bill()

    elif choice == "10":
        show_bill()

    elif choice == "11":
        final_slip()

    elif choice == "12":
        print("Thank You")
        break

    else:
        print("Wrong Choice")