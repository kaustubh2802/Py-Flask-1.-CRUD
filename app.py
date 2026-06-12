from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from database.db import get_connection

app = Flask(__name__)

@app.route("/")
def home():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    conn.close()

    return render_template("index.html",students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        conn = get_connection()

        cursor = conn.cursor()

        query = """INSERT INTO students(name,email,course)VALUES(%s,%s,%s)"""

        cursor.execute(
            query,
            (name,email,course)
        )

        conn.commit()

        conn.close()

        return redirect("/")

    return render_template(
        "add_student.html"
    )


@app.route("/delete/<int:id>")
def delete_student(id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )

    conn.commit()

    conn.close()

    return redirect("/")



@app.route(
    "/edit/<int:id>",
    methods=["GET","POST"]
)
def edit_student(id):

    conn = get_connection()

    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        query = """
        UPDATE students
        SET
        name=%s,
        email=%s,
        course=%s
        WHERE id=%s
        """

        cursor.execute(
            query,
            (name,email,course,id)
        )

        conn.commit()

        conn.close()

        return redirect("/")

    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (id,)
    )

    student = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_student.html",
        student=student
    )

if __name__ == "__main__":
    app.run(debug=True)


 