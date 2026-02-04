import os
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

subjects = {}
while True:
    os.system(ClearCommand)
    numOfSub = input("Input number of subjects in your semester: ")
    try:
        numOfSub = int(numOfSub)
        if numOfSub <=0:
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
            if subECTS <=0:
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


printSubjects(subjects)
print(f"Calculated average for this semester: {round(calcWeightedAverage(subjects),2)}")
input("Press ENTER to continue...")
