from setup import regular_course, course, color
arr = []

#repeating the gpa conversion for every course
#until I can figure out how to loop it and append it to the array properly
def first_course():
    print(color.UNDERLINE + color.PURPLE + "Course 1" + color.END)
    course1 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: "))
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
    course2 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: "))
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
    course3 = course(input("AP/Honors? " + color.YELLOW + color.BOLD + "YES (1) NO (2)" + color.END), input("Enter Grade: "))
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


#need to figure out how to use greater than less than with float
#possibly using a module
def final_output():
    sum_of = sum(arr)
    final_gpa = sum_of / 3
    print(final_gpa)

    ignation = print("Eligible for" + color.YELLOW + " Ignatian Honors " + color.END + "(4.0 and Above)")
    first = print("Eligible for" + color.BLUE + " First Honors " + color.END + "(3.600 to 3.999)")
    second = print("Eligible for" + color.BLUE + " Second Honors " + color.END + "(3.000 to 3.599)")

    if final_gpa >= 4.000:
        ignation
    elif final_gpa > 3.600 and final_gpa < 3.999:
        first
    elif final_gpa > 3.000 and final_gpa < 3.599:
        second
    else:
        print("")
final_output()

