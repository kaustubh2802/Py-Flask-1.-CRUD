# from flask import Flask
# from flask import render_template
# from flask import request
# from flask import redirect
# from database.db import get_connection



from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from database.db import get_connection
from flask import flash






app = Flask(__name__)

app.secret_key = "student_management_secret"




# app = Flask(__name__)

# @app.route("/")
# def home():

#     conn = get_connection()

#     cursor = conn.cursor()

#     cursor.execute(
#         "SELECT * FROM students"
#     )

#     students = cursor.fetchall()

#     conn.close()

#     return render_template("index.html",students=students)

@app.route("/")
def home():

    if 'user_id' not in session:
        return redirect('/login')

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students
    )





@app.route("/add", methods=["GET", "POST"])
def add_student():
    if 'user_id' not in session:
        return redirect('/login') 

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
    if 'user_id' not in session:
        return redirect('/login')

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
    if 'user_id' not in session:
        return redirect('/login')

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



@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        #password = abc@123

        # $4528sdaf8asdf54asdf43ds3f1 = generate_password_hash(password)
        hashed_password = generate_password_hash(password)

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO users(name,email,password)
        VALUES(%s,%s,%s)
        """

        cursor.execute(
            query,
            (name,email,hashed_password)
        )

        conn.commit()
        flash( "Registration Successful", "success")


        cursor.close()
        conn.close()

        return redirect('/login')

    return render_template('register.html')



@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT * FROM users
        WHERE email=%s
        """

        cursor.execute(query,(email,))

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(
                user['password'],
                password):

            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_email'] = email
            flash( "Login Successful", "success")

            return redirect('/')

        flash("Invalid Email or Password","error")
        # return "Invalid Email or Password"
    

    return render_template('login.html')
 


@app.route('/logout')
def logout():

    session.clear()

    flash(
        "Logout Successful",
        "success"
    )

    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)