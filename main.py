from flask import Flask, render_template, request
import smtplib
import os

own_email = os.environ.get("OWN_EMAIL")
own_password = os.environ.get("OWN_PASSWORD")


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, subject, message):
    email_message = f"Subject:{subject}\n\nEmail: {email}\nName: {name}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(own_email, own_password)
        connection.sendmail(own_email, own_email, email_message)


if __name__ == "__main__":
    app.run(debug=True)