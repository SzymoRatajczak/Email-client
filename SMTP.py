import smtplib
import sys

def SMTP():
    if len(sys.argv)<4:
        name=sys.argv[0]
        print('alert:',name)
        sys.exit()

    hostname=sys.argv[1]
    from_addr=sys.argv[2]
    to_addr=sys.argv[3]
    message='sample message'

    try:
        conn=smtplib.SMTP(hostname)
        conn.set_debuglevel(1)
        conn.sendmail(from_addr,to_addr,message)
    except smtplib.SMTPException as e:
        print("error:",e)
    finally:
        conn.quit()

SMTP()