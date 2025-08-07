attendance=int(input("How many days did you attend classes:"))
if attendance>=75:
    print("you are allowed to take exams")
else:
    medicalcause=input("were you sick?:")
    if medicalcause==("yes" or "YES"):
        print("you can take exams")
    else:
        print("you are not allowed to take exams")