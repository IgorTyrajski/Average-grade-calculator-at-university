import os
import csv
ClearCommand = "cls" if os.name == "nt" else "clear"

def calcArithmeticAverage(marks):
    numOfSubjects = 0
    sumMarks = 0
    for mark in marks:
        if isinstance(mark,(int, float)):
            numOfSubjects += 1
            sumMarks +=mark
    if numOfSubjects == 0:
        return 0
    return sumMarks/numOfSubjects

def calcWeightedAverage(subjects):
    sumECTS = 0
    sumGradeECTS = 0

    for sub in subjects.keys():
        sumECTS += subjects[sub][0]
        sumGradeECTS += calcArithmeticAverage(subjects[sub][1]) * subjects[sub][0]
    if sumGradeECTS == 0:
        return 0
    return sumGradeECTS/sumECTS

def printSubjects(subjects):
    if len(subjects.keys()) > 0:
        os.system(ClearCommand)
        for sub in subjects.keys():
            marks_list = subjects[sub][1]
            marks_string = ", ".join(map(str, marks_list))

            print(f"{sub}: {marks_string}")

def writeMarksToFile(subjects):
    with open('marks.csv','w',newline='') as f:
        fileWriter = csv.writer(f,delimiter=';')
        for subject in subjects.keys():
            row = [subject, subjects[subject][0]] + subjects[subject][1]
            fileWriter.writerow(row)


def readMarksFromFile(subjects):
    try:
        with open('marks.csv', 'r', newline='') as f:
            fileReader = csv.reader(f, delimiter=';')
            fileReader = list(fileReader)
            for row in fileReader:
                try:
                    name = str(row[0])
                    ects = int(row[1])
                    marks = []
                    for i in range(2,6):
                        try:
                            marks.append(float(row[i]))
                        except ValueError:
                            marks.append(str(row[i]))
                    subject = [ects, marks]
                    subjects[name] = subject
                except ValueError:
                    print("Reading file error")
    except:
        print("File open error")

def inputData(subjects):
    while True:
        os.system(ClearCommand)
        numOfSub = input("Input number of subjects in your semester: ")

        try:
            numOfSub = int(numOfSub)
            if numOfSub <= 0:
                print("Please input a correct value")
                input("Press ENTER to continue...")

            else:
                break
        except ValueError:
            print("Please input a number")
            input("Press ENTER to continue...")

    for i in range(numOfSub):
        while True:
            error = False

            printSubjects(subjects)

            subName = str(input("Input subjects name: "))
            subECTS = input("Input subjects ECTS value: ")
            try:
                subECTS = int(subECTS)
                if subECTS <= 0:
                    print("Please correct ECTS value ")
                    error = True
                    continue
            except ValueError:
                print("Please input ECTS value as a number")
                error = True
                continue

            marks = []
            marks.append(input("Input mark for lecture (input 'x' if did not have lectures): "))
            marks.append(input("Input mark for laboratories (input 'x' if did not have laboratories): "))
            marks.append(input("Input mark for classes (input 'x' if did not have classes): "))
            marks.append(input("Input mark for project (input 'x' if did not have project classes): "))

            for j in range(len(marks)):
                try:
                    marks[j] = float(marks[j])
                    if marks[j] < 2.0 or marks[j] > 5.0:
                        print("Grades input incorrect")
                        input("Press ENTER to continue...")
                        error = True
                        break
                except ValueError:
                    marks[j] = 'x'
            if not error:
                subject = [subECTS, marks]
                subjects[subName] = subject
                break

def editData(subjects):
    os.system(ClearCommand)
    printSubjects(subjects)
    sub = str(input("Which subject data would you like to modify: "))
    while True:
        if sub not in subjects.keys():
            sub = str(input("Which subject data would you like to modify: "))
        else:
            break

    while True:
        error = False
        print("\n")
        print(f"Ects for {sub}: {subjects[sub][0]}")
        print(f"1. Lecture: {subjects[sub][1][0]}")
        print(f"2. Laboratories: {subjects[sub][1][1]}")
        print(f"3. Classes: {subjects[sub][1][2]}")
        print(f"4. Project classes: {subjects[sub][1][3]}")
        print("Which info would you like to change: ")
        markOpt = input("Input 1 for lecture, 2 for labs and etc.: ")
        try:
            markOpt = int(markOpt)
            if markOpt > 4 or markOpt < 1:
                print("Input correct value")
                error = True
        except ValueError:
            error = True
            print("Input correct data")
            continue

        newMark = input("Input new mark: ")
        try:
            newMark = float(newMark)
            if newMark > 5 or newMark < 2:
                print("Input correct value")
                error = True
        except ValueError:
            newMark = 'x'

        if error == False:
            subjects[sub][1][markOpt - 1] = newMark
            break

subjects = {}
os.system(ClearCommand)
print("Options: ")
print("1. Insert new data")
print("2. Modify last data")
print("3. Print last data")
opt = input("What would you like to do: ")
if opt == '1':
    inputData(subjects)
elif opt == '2':
    readMarksFromFile(subjects)
    editData(subjects)
    os.system(ClearCommand)
    printSubjects(subjects)
elif opt == '3':
    readMarksFromFile(subjects)
    printSubjects(subjects)
else:
    print("Please input correct option")

writeMarksToFile(subjects)

print(f"Calculated average for this semester: {round(calcWeightedAverage(subjects),2)}")
input("Press ENTER to continue...")
