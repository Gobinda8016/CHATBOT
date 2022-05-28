import email
from flask import Flask, render_template, jsonify, request
import processor
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="remotemysql.com", user="eYvIUyXdHW", password="n0m4CLl2X5", database="eYvIUyXdHW")

cursor = conn.cursor()

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route("/Login")
def Login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blogpost")
def blogpost():
    return render_template("blogpost.html")


@app.route("/blogpost2")
def blogpost2():
    return render_template("blogpost2.html")


@app.route("/blogpost3")
def blogpost3():
    return render_template("blogpost3.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/Login/registration")
def signup():
    return render_template("registration.html")


@app.route("/registration/login")
def signin():
    return render_template("Login.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['msg']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response})
# For_Login


@app.route('/login_validation', methods=['POST'])
def login_validation():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute(
        """SELECT * FROM `Registration` WHERE `username` LIKE '{}' AND `password` LIKE '{}'""".format(username, password))
    users = cursor.fetchall()
    print(users)
    return render_template('index.html')

# Adding User Information into Database


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('usernamea')
    email = request.form.get('emaila')
    password = request.form.get('passworda')
    cursor.execute("""INSERT INTO `Registration` (`username`,`email`,`password`) VALUES ('{}','{}','{}')""".format(
        username, email, password))
    conn.commit()
    return render_template('index.html')


@app.route('/add_contact', methods=['POST'])
def add_contact():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    country = request.form.get('country')
    subject = request.form.get('subject')
    cursor.execute("""INSERT INTO `Contact Form`  (`firstname`,`lastname`,`country`, `subject`) VALUES ('{}','{}','{}', '{}')""".format(
        firstname, lastname, country, subject))
    conn.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
