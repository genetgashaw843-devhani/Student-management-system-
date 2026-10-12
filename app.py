
from flask import Flask, request, redirect

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return """
    <h1>Student Management System</h1>
    <form action="/add" method="post">
        <input name="name" placeholder="Student Name" required>
        <input name="student_id" placeholder="Student ID" required>
        <button type="submit">Add Student</button>
    </form>
    <h2>Student List</h2>
    """ + "".join(
        f"<p>{s['student_id']} - {s['name']}</p>"
        for s in students
    )

@app.route("/add", methods=["POST"])
def add_student():
    students.append({
        "name": request.form["name"],
        "student_id": request.form["student_id"]
    })
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
