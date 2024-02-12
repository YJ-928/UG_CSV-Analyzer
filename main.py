from data import count
import pandas as pd

#Number of rows and columns in phase1.csv and phase2.csv
r1 = count.get_row1()
r2 = count.get_row2()
c1 = count.get_column1()
c2 = count.get_column2()

#fetch csv data and convert it to 1D array using Pandas.
phase1 = count.get_Phase1()
phase1 = pd.Series(data = phase1)
phase2 = count.get_Phase2()
phase2 = pd.Series(data = phase2)

anemic1 = [] #Lists of Patient's IDs suffering anemia
unidentified1 = [] #Lists of Patient's who have not give Hb tests
non_anemic1 = [] #Lists of Patient's IDs not suffering anemia

#Detect Anemic Patients using Hb(1st Obs) column...
for i in range(r1):
    i += 1
    try:
        x = float(phase1[i][2])
    except ValueError:
        x = 0

    if x <= 12.0 and x != 0:
        anemic1.append(phase1[i][0])
    elif x == 0:
        unidentified1.append(phase1[i][0])
    else:
        non_anemic1.append(phase1[i][0])

anemic2 = [] #Lists of Patient's IDs suffering anemia in 2nd obs
unidentified2 = [] #Lists of Patient's who have not give Hb tests in 2nd obs
non_anemic2 = [] #Lists of Patient's IDs not suffering anemia in 2nd obs

#Detect Anemic Patients using Hb(Phase 2) column...
for i in range(r2):
    i += 1
    try:
        x = float(phase2[i][1])
    except ValueError:
        x = 0

    if x <= 12.0 and x != 0:
        anemic2.append(phase2[i][0])
    elif x == 0:
        unidentified2.append(phase2[i][0])
    else:
        non_anemic2.append(phase2[i][0])

#Print the results...
print("\n      ")
print(f"Total number of people in Phase 1 = {r1}")
print(f"Number of people suffering from anemia in phase 1 = {len(anemic1)}")
print(f"Number of people who have not reported to doctors = {len(unidentified1)}")
if len(anemic1) == 0:
    print("No anemic Patients detected.")
else:
    print("List of patient's ID suffering from Anemia are;")
    for ID in anemic1:
        print(ID)

print("\n      ")

print(f"Total number of people in Phase 2 = {r2}")
print(f"Number of people suffering from anemia in phase 2 = {len(anemic2)}")
print(f"Number of people who have not reported to doctors = {len(unidentified1)}")
if len(anemic2) == 0:
    print("No anemic Patients detected.")
else:
    print("List of patient's ID suffering from Anemia are;")
    for ID in anemic2:
        print("People suffering from anemia are;")
        print(ID)

print("\n      ")