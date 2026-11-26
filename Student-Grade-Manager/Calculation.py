from add_exams import grades

def calculate_QZ_Average():

    fall_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Quiz"
        and grade["semester"] == "Fall"
    ]

    spring_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Quiz"
        and grade["semester"] == "Spring"
    ]

    fall_average = (
        sum(fall_grades) / len(fall_grades) * 0.15
        if fall_grades else 0
    )

    spring_average = (
        sum(spring_grades) / len(spring_grades) * 0.15
        if spring_grades else 0
    )

    return {
        "Fall Quiz Average": round(fall_average, 2),
        "Spring Quiz Average": round(spring_average, 2)
    }

def calculate_WA_Average():

    fall_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Writing"
        and grade["semester"] == "Fall"
    ]

    spring_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Writing"
        and grade["semester"] == "Spring"
    ]

    fall_average = (
        sum(fall_grades) / len(fall_grades) * 0.05
        if fall_grades else 0
    )

    spring_average = (
        sum(spring_grades) / len(spring_grades) * 0.05
        if spring_grades else 0
    )

    return {
        "Fall Writing Average": round(fall_average, 2),
        "Spring Writing Average": round(spring_average, 2)
    }

def calculate_SA_Average():

    fall_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Speaking Assessment"
        and grade["semester"] == "Fall"
    ]

    spring_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Speaking Assessment"
        and grade["semester"] == "Spring"
    ]

    fall_average = (
        sum(fall_grades) / len(fall_grades) * 0.05
        if fall_grades else 0
    )

    spring_average = (
        sum(spring_grades) / len(spring_grades) * 0.05
        if spring_grades else 0
    )

    return {
        "Fall Speaking Average": round(fall_average, 2),
        "Spring Speaking Average": round(spring_average, 2)
    }

def calculate_MID_Average():

    fall_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Midterm"
        and grade["semester"] == "Fall"
    ]

    spring_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Midterm"
        and grade["semester"] == "Spring"
    ]

    fall_average = (
        sum(fall_grades) / len(fall_grades) * 0.20
        if fall_grades else 0
    )

    spring_average = (
        sum(spring_grades) / len(spring_grades) * 0.25
        if spring_grades else 0
    )

    return {
        "Fall Midterm Average": round(fall_average, 2),
        "Spring Midterm Average": round(spring_average, 2)
    }

def calculate_SE_Average():

    spring_grades = [
        grade["Grade"]
        for grade in grades
        if grade["Exam Type"] == "Speaking Examination"
        and grade["semester"] == "Spring"
    ]

    spring_average = (
        sum(spring_grades) / len(spring_grades) * 0.05
        if spring_grades else 0
    )

    return {
        "Spring Speaking Examination Average": round(spring_average, 2)
    }

def calculate_final_grade():

    quiz_average = calculate_QZ_Average()
    writing_average = calculate_WA_Average()
    speaking_average = calculate_SA_Average()
    midterm_average = calculate_MID_Average()
    speaking_exam_average = calculate_SE_Average()

    final_grade = (
        quiz_average["Fall Quiz Average"] +
        quiz_average["Spring Quiz Average"] +
        writing_average["Fall Writing Average"] +
        writing_average["Spring Writing Average"] +
        speaking_average["Fall Speaking Average"] +
        speaking_average["Spring Speaking Average"] +
        midterm_average["Fall Midterm Average"] +
        midterm_average["Spring Midterm Average"] +
        speaking_exam_average.get("Spring Speaking Examination Average", 0)
    )

    return round(final_grade, 2)
