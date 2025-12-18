# main.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, recipient, subject, body):
    try:
        # Create message
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server (example)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure connection
        server.login(sender, password)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

def main():
    print("📧 Email Sender")
    sender = input("Enter your email: ")
    password = input("Enter your email password (use app password if required): ")
    recipient = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    body = input("Enter message body: ")

    send_email(sender, password, recipient, subject, body)

if __name__ == "__main__":
    main()
