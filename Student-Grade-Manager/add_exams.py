def choose_the_exam_type(choice_exam=None):
    return choice_exam


def choose_the_exam_no(choice_no):
    choice_no = str(choice_no)

    if len(choice_no) == 2 and choice_no.isdigit():
        return choice_no
    else:
        raise ValueError(
            "Exam number must contain exactly two digits!"
        )


def choose_the_exam_term(choice_semester=None):
    return choice_semester


def validate_grade(grade):
    if 0 <= grade <= 100:
        return grade
    else:
        raise ValueError("Grade must be between 0 and 100.")


grades = []


# ADD GRADE
def add_grade(exam_type, exam_no, exam_semester, grade):

    try:
        exam_type = choose_the_exam_type(exam_type)
        exam_no = choose_the_exam_no(exam_no)
        exam_semester = choose_the_exam_term(exam_semester)
        grade = validate_grade(grade)

        if exam_type == "Speaking Examination" and exam_semester == "Fall":
            raise ValueError("Speaking Examination is only available in Spring semester!")

        new_grade = {
            "Exam Type": exam_type,
            "Exam No": exam_no,
            "Exam": f"{exam_type}{exam_no}",
            "semester": exam_semester,
            "Grade": grade
        }

        grades.append(new_grade)

        return new_grade

    except ValueError as error:
        return str(error)


# DELETE GRADE
def delete_grade(exam_type, exam_no, exam_semester):
    for grade in grades:
        if (grade["Exam Type"] == exam_type and grade["Exam No"] == str(exam_no) and grade["semester"] == exam_semester):
            grades.remove(grade)
            return True


