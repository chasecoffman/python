from setup import regular_course, course, color
arr = []


i = 1
while i <= 7:
    def courses():
        print(color.UNDERLINE + color.PURPLE + "Course" + color.END,i)
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
        courses()

    i += 1
    courses()


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
