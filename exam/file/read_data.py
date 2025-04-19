class people:
    SNo = int
    Age = int
    Sex = ""
    Ethnicity = ""
    BMI = float
    Waist_Circumference = float
    Fasting_Blood_Glucose = float
    HbA1c = float
    Blood_Pressure_Systolic = int
    Blood_Pressure_Diastolic = int
    Cholesterol_Total = float
    Cholesterol_HDL = float
    Cholesterol_LDL = float
    GGT = float
    Serum_Urate = float
    Physical_Activity_Level = ""
    Dietary_Intake_Calories = int
    Alcohol_Consumption = ""
    Smoking_Status = ""
    Family_History_of_Diabetes = int
    Previous_Gestational_Diabetes = int

def diabetics_data():
    list = []
    count = 0
    for line in open("diabetes_dataset.csv"):
        if count == 0:
            count += 1
            continue
        peopleArr = line.split(',')

        if len(peopleArr) < 22:
            print(f"Skipping incomplete line {count}: {peopleArr}")
            count += 1
            continue
        objpeople = people()
        objpeople.SNo = peopleArr[1]
        objpeople.Age = peopleArr[2]
        objpeople.Sex = peopleArr[3]
        objpeople.Ethnicity = peopleArr[4]
        objpeople.BMI = peopleArr[5]
        objpeople.Waist_Circumference = peopleArr[6]
        objpeople.Fasting_Blood_Glucose = peopleArr[7]
        objpeople.HbA1c = peopleArr[8]
        objpeople.Blood_Pressure_Systolic = peopleArr[9]
        objpeople.Blood_Pressure_Diastolic = peopleArr[10]
        objpeople.Cholesterol_Total = peopleArr[11]
        objpeople.Cholesterol_HDL = peopleArr[12]
        objpeople.Cholesterol_LDL = peopleArr[13]
        objpeople.GGT = peopleArr[14]
        objpeople.Serum_Urate = peopleArr[15]
        objpeople.Physical_Activity_Level = peopleArr[16]
        objpeople.Dietary_Intake_Calories = peopleArr[17]
        objpeople.Alcohol_Consumption = peopleArr[18]
        objpeople.Smoking_Status = peopleArr[19]
        objpeople.Family_History_of_Diabetes = peopleArr[20]
        objpeople.Previous_Gestational_Diabetes = peopleArr[21]

diabetics_data()






