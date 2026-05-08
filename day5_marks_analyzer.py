def students_mark_analyzer(records: list):
    expected_output = {}

    for record in records:
        student_name, subject, marks = record.split("|")

        student_name = student_name.strip()
        subject = subject.strip()
        marks = int(marks.strip())

        if student_name not in expected_output:
            expected_output[student_name] = {}

        expected_output[student_name][subject] = marks

    return expected_output


records = [
    "Alice | Math | 85",
    "Bob | Science | 90",
    "Alice | Science | 78",
    "Bob | Math | 95",
    "Carol | Math | 88"
]

print(students_mark_analyzer(records))