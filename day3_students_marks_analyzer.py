def marks_analyzer(records: list):
    #parse each record and extract values
    new_record ={}
    for record in records:
        name,subject,marks= record.split("|")
        name = name.strip()
        subject = subject.strip()
        marks = int(marks.strip())
        if name not in new_record:
            new_record[name] = {}
        new_record[name][subject] = marks
    
    total= {}  
    for outer_key, inner_dict in new_record.items():
        total_sum = 0  
        for value in inner_dict.values():
            total_sum += value
        total[outer_key] = total_sum
        
    top_scorer = None
    max_value = 0
    for key, value in total.items():
        if value > max_value:
            top_scorer = key
            max_value = value
        
    return {
    "student_marks": new_record,
    "totals":total,
    "top_scorer": (top_scorer,max_value)
}
        
records = [
    "Alice | Math | 85",
    "Bob | Science | 90",
    "Alice | Science | 78",
    "Bob | Math | 95",
    "Carol | Math | 88"
]

print(marks_analyzer(records))