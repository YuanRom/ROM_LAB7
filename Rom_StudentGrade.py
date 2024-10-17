name = input("Put your name: ")
section = input("Put your section: ")
prelim = float(input("Input prelim Grade: "))
if prelim < 40 or prelim > 100:
    print ("Invalid grade")
    exit ()
midterm = float(input("Input midterm Grade: "))
if midterm < 40 or prelim > 100:
    print ("Invalid grade")
    exit ()
finals = float(input("Input finals Grade: "))
if finals < 40 or prelim > 100:
    print ("Invalid grade")
    exit ()
finals_grade = (prelim * .3333) +  (midterm * .3333 ) + (finals * .3333)
print(f"Final grade for this semester: {finals_grade: .0f}")


if finals_grade > 99 and finals_grade < 100:
    print ("GPA is 1.00")
elif finals_grade > 96 and finals_grade < 98:
    print ("GPA is 1.25")
elif finals_grade > 93 and finals_grade < 95:
    print ("GPA is 1.50")
elif finals_grade > 90 and finals_grade < 92:
    print ("GPA is 1.75")
elif finals_grade > 87 and finals_grade < 89:
    print ("GPA is 2.00")
elif finals_grade > 84 and finals_grade < 86:
    print ("GPA is 2.25")
elif finals_grade > 81 and finals_grade < 83:
    print ("GPA is 2.50")
elif finals_grade > 78 and finals_grade < 80:
    print ("GPA is 2.75")
elif finals_grade > 75 and finals_grade < 77:
    print ("GPA is 3.00")
elif finals_grade > 1 and finals_grade < 75 :
    print ("GPA is 5.0")