from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route("/Login")
def Login():
    return render_template("login.html")


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
