from datetime import datetime

name = "Surendra"

now = datetime.now()

date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")

already_marked = False

with open("attendance.csv", "r") as file:
    records = file.readlines()

for record in records:
    if name in record and date in record:
        already_marked = True
        break

if not already_marked:
    with open("attendance.csv", "a") as file:
        file.write(f"{name},{date},{time}\n")

    print("Attendance Marked!")
else:
    print("Attendance Already Marked Today")