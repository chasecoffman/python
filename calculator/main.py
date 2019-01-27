from setup import regular_course, course, color
arr = []

#repeating the gpa conversion for every course
#until I can figure out how to loop it and append it to the array properly

def first_course():
    print(color.UNDERLINE + color.PURPLE + "Course 1" + color.END)
    course1 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: ").upper())
    ap_honors_course = (regular_course[course1.grade]) + 1.0

    if course1.is_regular == "1" and course1.grade in regular_course:
        if ap_honors_course <= 3.3:
            arr.append(regular_course[course1.grade])
        else:
            arr.append(ap_honors_course)

    elif course1.is_regular == "2" and course1.grade in regular_course:
        arr.append(regular_course[course1.grade])
    else:
        print("Invalid Grade")
        first_course()

first_course()

def second_course():
    print(color.UNDERLINE + color.PURPLE + "Course 2" + color.END)
    course2 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: ").upper())
    ap_honors_course = (regular_course[course2.grade]) + 1.0

    if course2.is_regular == "1" and course2.grade in regular_course:
        if ap_honors_course <= 3.3:
            arr.append(regular_course[course2.grade])
        else:
            arr.append(ap_honors_course)

    elif course2.is_regular == "2" and course2.grade in regular_course:
        arr.append(regular_course[course2.grade])
    else:
        print("Invalid Grade")
        second_course()

second_course()

def third_course():
    print(color.UNDERLINE + color.PURPLE + "Course 3" + color.END)
    course3 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: ").upper())
    ap_honors_course = (regular_course[course3.grade]) + 1.0

    if course3.is_regular == "1" and course3.grade in regular_course:
        if ap_honors_course <= 3.3:
            arr.append(regular_course[course3.grade])
        else:
            arr.append(ap_honors_course)

    elif course3.is_regular == "2" and course3.grade in regular_course:
        arr.append(regular_course[course3.grade])
    else:
        print("Invalid Grade")
        third_course()

third_course()

def fourth_course():
    print(color.UNDERLINE + color.PURPLE + "Course 4" + color.END)
    course4 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: ").upper())
    ap_honors_course = (regular_course[course4.grade]) + 1.0

    if course4.is_regular == "1" and course4.grade in regular_course:
        if ap_honors_course <= 3.3:
            arr.append(regular_course[course4.grade])
        else:
            arr.append(ap_honors_course)

    elif course4.is_regular == "2" and course4.grade in regular_course:
        arr.append(regular_course[course4.grade])
    else:
        print("Invalid Grade")
        fourth_course()

fourth_course()

def fifth_course():
    print(color.UNDERLINE + color.PURPLE + "Course 5" + color.END)
    course5 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: ").upper())
    ap_honors_course = (regular_course[course5.grade]) + 1.0

    if course5.is_regular == "1" and course5.grade in regular_course:
        if ap_honors_course <= 3.3:
            arr.append(regular_course[course5.grade])
        else:
            arr.append(ap_honors_course)

    elif course5.is_regular == "2" and course5.grade in regular_course:
        arr.append(regular_course[course5.grade])
    else:
        print("Invalid Grade")
        fifth_course()

fifth_course()

def sixth_course():
    print(color.UNDERLINE + color.PURPLE + "Course 6" + color.END)
    course6 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: ").upper())
    ap_honors_course = (regular_course[course6.grade]) + 1.0

    if course6.is_regular == "1" and course6.grade in regular_course:
        if ap_honors_course <= 3.3:
            arr.append(regular_course[course6.grade])
        else:
            arr.append(ap_honors_course)

    elif course6.is_regular == "2" and course6.grade in regular_course:
        arr.append(regular_course[course6.grade])
    else:
        print("Invalid Grade")
        sixth_course()

sixth_course()

def seventh_course():
    print(color.UNDERLINE + color.PURPLE + "Course 7" + color.END)
    course7 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: ").upper())
    ap_honors_course = (regular_course[course7.grade]) + 1.0

    if course7.is_regular == "1" and course7.grade in regular_course:
        if ap_honors_course <= 3.3:
            arr.append(regular_course[course7.grade])
        else:
            arr.append(ap_honors_course)

    elif course7.is_regular == "2" and course7.grade in regular_course:
        arr.append(regular_course[course7.grade])
    else:
        print("Invalid Grade")
        seventh_course()

seventh_course()


def final_output():
    sum_of = sum(arr)
    final = sum_of / 7
    final_gpa = round(final, 7)
    print(final_gpa)

    if float(final_gpa) >= 4.000:
        print("Eligible for" + color.YELLOW + " Ignatian Honors " + color.END + "(4.0 and Above)")
    elif float(final_gpa) > 3.600 and float(final_gpa) < 3.999:
        print("Eligible for" + color.BLUE + " First Honors " + color.END + "(3.600 to 3.999)")
    elif float(final_gpa) > 3.000 and float(final_gpa) < 3.599:
        print("Eligible for" + color.BLUE + " Second Honors " + color.END + "(3.000 to 3.599)")
    else:
        print("Not Eligible for any Honors at this time.")
final_output()
