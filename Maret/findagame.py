import psycopg2

try:
    conn = psycopg2.connect("dbname='findagame' user='postgres' password='admin'")
except:
    print("I am unable to connect to the database.")
cur = conn.cursor()
try:
    cur.execute('''select * from accounts;''')
except:
    print("I can't drop our test database!")
result = cur.fetchall()
login = False
while login == False:
    uname = input("Username: ")
    pswd = input("Password: ")
    for i in range (len(result)):
        uname_server = result[i][1]
        pswd_server = result[i][2]
        if uname == uname_server and pswd == pswd_server:
            login = True
    if login == True:
        print("Berhasil Login")
    else:
        print("uname/password salah")

