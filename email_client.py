import socket
import smtplib
import sys

def email_client():
    if len(sys.argv)<4:
        name=sys.argv[0]
        print('alert:',name)
        sys.exit()

    server=sys.argv[1]
    from_addr=sys.argv[2]
    to_addr=sys.argv[3]
    message="sample message"

    try:
        connection=smtplib.SMTP(server)
        connection.set_debuglevel(1)
        connection.sendmail(from_addr,to_addr,message)
    except(socket.error,socket.gaierror,socket.herror,smtplib.SMTPException) as e:
        print("error:",e)
    else:
        connection.quit()


email_client()

