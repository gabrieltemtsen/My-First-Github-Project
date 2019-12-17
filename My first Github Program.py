def gpa():
    courses = int(input("How many courses have you offered so far:"))
    course_limit = 0
    wgp = 0
    total_credit = 0

    for numbers in range(course_limit, courses):
        print ("Enter score for course ", numbers+1)
        score = int(input())
        print("Enter Credit Unit for course: ", numbers+1)
        credit_unit = int(input())
        if score >= 70 and score <= 100:
            grade = 5
            wgp += credit_unit * grade
            total_credit += credit_unit
        elif score >= 60 and score <= 69:
            grade = 4
            wgp += credit_unit * grade
            total_credit += credit_unit
        elif score >= 50 and score <= 59:
            grade = 3
            wgp += credit_unit * grade
            total_credit += credit_unit
        elif score >= 45 and score <= 49:
            grade = 2
            wgp += credit_unit * grade
            total_credit += credit_unit
        elif score >= 40 and score <= 44:
            grade = 1
            wgp += credit_unit * grade
            total_credit += credit_unit
        elif score >= 0 and score <= 39:
            grade = 0
            wgp += credit_unit * grade
            total_credit += credit_unit
        else:
            print("Sorry oo! start again")
    gpa = wgp / total_credit
    if gpa >= 4.5:
        print("Congratulations your Gpa is " + str(gpa) + " You are a first Class")
    if gpa >= 3.5 and gpa <= 4.44:
        print("Congratulations your Gpa is " + str(gpa) + " You are a second class upper student")
    if gpa >= 2.5 and gpa <= 3.49:
        print("Congratulations your Gpa is " + str(gpa) + " You are a second class lower student")
    if gpa >= 1.5 and gpa <= 2.49:
        print("Congratulations your Gpa is " + str(gpa) + " You are a Third class student")
    if gpa >= 0 and gpa <= 1.49:
        print("Sorry your Gpa is " + str(gpa) + " You are a last lower student")



gpa()
# dict = ()
# counts = dict
# print(type(counts))



