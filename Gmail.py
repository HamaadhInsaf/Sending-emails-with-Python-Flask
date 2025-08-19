from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Now you can safely access your environment variables
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("GMAIL_MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("GMAIL_MAIL_PASSWORD")

mail = Mail(app)

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Flask Email Sender</title>
        </head>
    <body>
        <h1>Welcome to the Flask email sender!</h1>
        <p>To send an email to yourself, add <em>/send-email/yourname@example.com</em> to the URL bar</p>
    </body>
    </html>
    """

@app.route("/send-email")
def send_email_bad_request():
    return """
    <html>
        <head>
            <title>Bad Request</title>
        </head>
    <body>
        <h1>Error 400 - Bad Request</h1>
        <p>To send an email to yourself, add <em>/send-email/yourname@example.com</em> to the URL bar</p>
    </body>
    </html>
    """

@app.route("/send-email/<recipient_email>")
def send_email(recipient_email):
    msg = Message(
        subject = "Hello from Gmail servers!",
        sender=app.config["MAIL_USERNAME"],
        recipients = [recipient_email],
        body = "This is a test email sent from Gmail servers using Flask."
    )
    mail.send(msg)
    return f"""
    <html>
        <head>
            <title>Email Sent</title>
        </head>
    <body>
        <h2>Email sent to {recipient_email}!</h2>
    </body>
    </html>
    """

# Start the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)