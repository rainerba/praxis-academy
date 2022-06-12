import psycopg2
uname = ""
olahraga = ""
nama_gor = ""
gor_id = 0
jam_booking = 0
orang = 0
try:
    conn = psycopg2.connect("dbname='findagame' user='postgres' password='admin'")
except:
    print("I am unable to connect to the database.")
def kursor(psql):
    cur = conn.cursor()
    cur.execute(psql)
    return cur.fetchall()

def login():
    try:
        akun = kursor('''select * from accounts;''')
    except:
        print("I can't drop accounts database!")
    login = False
    while login == False:
        uname = input("Username: ")
        pswd = input("Password: ")
        for i in range (len(akun)):
            uname_server = akun[i][1]
            pswd_server = akun[i][2]
            if uname == uname_server and pswd == pswd_server:
                login = True
        if login == True:
            print("Berhasil Login")
        else:
            print("uname/password salah")
# login()
def show_olahraga():
    try:
        result = kursor('''select distinct olahraga from gor;''')
        print("Olahraga Tersedia: ")
        print(result)
    except:
        print("I can't drop olahraga database!")
show_olahraga()
def booking_olahraga():
    olahraga = input("Mau booking olahraga apa? ")
    try:
        result = kursor('''select nama_gor, harga from gor where olahraga = '{}';'''.format(olahraga))
        print("Lapangan tersedia: ")
        print(result)
    except:
        print("I can't drop data lapangan gor tersedia database!")
booking_olahraga()
def booking_tempat():
    nama_gor = input("Mau Booking Dimana? ")
    try:
        result = kursor('''select gor_id, nama_gor, harga from gor where nama_gor = '{}' and olahraga ='{}';'''.format(nama_gor, olahraga))
        print(result)
    except:
        print("I can't drop data booking database!")
booking_tempat()
# def booking_jam_dan_orang():
#     try:
#         min_orang = kursor('''select min_orang from gor;''')
#         result = kursor(
#             '''select nama_gor, jam_booking, jumlah_orang from data_booking
#             where nama_gor = '{}' and olahraga ='{}' and jumlah_orang >= {};'''.format(nama_gor, olahraga, min_orang)
#             )
#         print("Jam yang sudah di-booking:")
#         print(result)
#         # jam_booking = input("Booking jam Berapa? ")
#         # orang = input("Reservasi untuk berapa orang? ")
#     except:
#         print("I can't drop Jam yang sudah di-booking database!")
# booking_jam_dan_orang()

# try:
#     gor_id = kursor('''select gor_id from gor where olahraga = '{olahraga}' and nama_gor = '{nama}';''')
#     kursor(
#         '''insert into data_booking(gor_id, uname, jam_booking, olahraga, nama_gor)
#         values
#         ;'''
#     )
# except:
#     print("I can't send and receive data booking database!")