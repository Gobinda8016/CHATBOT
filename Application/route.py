from Application import app
from flask.helpers import url_for
from werkzeug.utils import redirect
from chatbot import chatbot
from flask import Flask, render_template, request
@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/chat")
def chat():
    return render_template("chat.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
if __name__=="__main__":
      app.run(debug=True,port=5000)