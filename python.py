import smtplib

def send_test_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('amsp33478@gmail.com','jyie pmvy fwyx subn')  # Use app password here
        server.sendmail('amsp33478@gmail.com', 'amsp604@gmail.com', 'Test email from Python')
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
 
send_test_email()