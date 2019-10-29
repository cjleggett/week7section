from cs50 import get_string, SQL

db = SQL("sqlite:///students.db")

# Add new person
name = get_string("Name: ")
student_id = db.execute("INSERT INTO people (name) VALUES (?)", name)

# Prompt for courses to enroll in
while True:
    code = get_string("Course Code: ")

    # If no input, then stop adding courses
    if not code:
        break

    # Query for course
    results = db.execute("SELECT id FROM courses WHERE code = ?", code)

    # Check to make sure course exists
    if len(results) == 0:
        print(f"No course with code {code}.")
        continue

    # Enroll student
    db.execute("INSERT INTO students (person_id, course_id) VALUES (?, ?)", student_id, results[0]["id"])
    print(f"Added {name} to {code}")
