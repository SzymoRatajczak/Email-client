import poplib
import sys
import getpass
import poplib
def POP3():
    if len(sys.argv)!=3:
        name=sys.argv[0]
        print("alert:",name)
        sys.exit()

    hostname,username=sys.argv[1:]

    conn=poplib.POP3_SSL(hostname)

    try:
        conn.user(username)
        conn.pass_(getpass.getpass())

    except poplib.Error as e:
        print("error:",e)
    else:
        status=conn.stat()
        print("Status:",status)
    finally:
        conn.close()


POP3()