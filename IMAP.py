import getpass
from imapclient import IMAPClient
import sys

def IMAP4():
    if len(sys.argv)!=3:
        name=sys.argv[0]
        print('alert:',name)
        sys.exit()

    hostname,username=sys.argv[1:]

    conn=IMAPClient(hostname,ssl=True)

    try:
        conn.login(username,getpass.getpass())

    except conn.Error as e:
        print("error:",e)

    else:
        directories=conn.select_folder()
        for i in directories:
            print(i)
    finally:
        conn.logout()


IMAP4()
