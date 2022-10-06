### Program Kasbon ### 
__author__ = "Moh.Jeli almuta'ali"
__version__ = 0.1

import os,sys
import mysql.connector

db = mysql.connector.connect(
        user ='meyza',
        password ='Jeli12345',
        host ='127.0.0.1',
        database='kasbon_db'
)
def menu():
    print("""
########################################
### Selamat datang di program Kasbon ###
########################################
1. Tampilkan data kasbon
2. Tambah data kasbon
3. Hapus data kasbon
4. Bayar Kasbon
5. Tambah Kasbon
        """)
    run = True
    while run:
        pilih = input('Pilih: ')
        if pilih == "1":
            run = False
            show_data(db)
        elif pilih == "2":
            run = False
            insert_data(db)
        elif pilih == "3":
            run = False
            delete_data(db)
        elif pilih == "4":
            run = False
            bayar_kasbon(db)
        elif pilih == "5":
            run = False
            tambah_kasbon(db)
        else:
            print("Input invalid")
        

def show_data(db):
    "Menampilkan data kasbon" 
    cursor = db.cursor()
    sql = "SELECT * FROM kasbon"
    cursor.execute(sql)
    result = cursor.fetchall()
    os.system('clear')
    print("+","-"*30)
    print("| No\t", "Nama\t", "\tTotal")
    print("+","-"*30)
    no_urut = 1
    for id, nama,total in result:
        print(" ",no_urut,"\t", nama.title(),"\t", "\t",total)
        no_urut += 1
    cursor.close()
    
    

def insert_data(db):
    run = True
    jum = 0
    while run:
        cursor = db.cursor()
        
        input_nama = input("Masukkan nama: ").capitalize()
        input_kasbon = input("Masukkan jumlah kasbon: ").capitalize()
    
        val = (None, input_nama, input_kasbon)
        sql = "INSERT INTO kasbon values(%s, %s, %s)"
        jum += 1
        pilih = input("Tambah data kasbon lagi? y or n: ")
        if pilih == "y":
            run = True
        elif pilih == "n":
            run = False
        else:
            print("input tidak valid")
        
    
        
    cursor.execute(sql,val)
    db.commit()
    print(f"Data yang berhasil disimpan: {jum}")
        
    

def delete_data(db):
    run = True
    jum = 0
    while run:
        cursor = db.cursor()
        show_data(db)
        sql_id = "SELECT id FROM kasbon"
        cursor.execute(sql_id)
        result_id = cursor.fetchall()
        
        ids = []
        for id in result_id:
            id = list(id)
            ids.append(id)  

        
        print("\nPilih nomer yang akan di hapus")

        
        no_id = input("Masukkan no: ")
        no_posisi = int(no_id) - 1
        
        sql = "DELETE FROM kasbon where id=%s"
        val = (ids[no_posisi][0],)

        jum +=1
        cursor.execute(sql,val)
        
        
        lagi = input("Hapus data lagi? y or n: ")
        if lagi == "y":
            run = True
        elif lagi == "n":
            run = False
        else:
            print("input tidak valid")
        
    db.commit()
    print(f"Data berhasil di hapus {jum}")   

def bayar_kasbon(db):
    cursor = db.cursor()
    show_data(db)
    sql_id = "SELECT * FROM kasbon"
    cursor.execute(sql_id)
    result = cursor.fetchall()
    
    data_kasbon = []
    # totals = []
    for data in result:
        data = list(data)
        # total = list(total)
        data_kasbon.append(data) 
        # totals.append(total)
    
    print("\n\n\n\nPilih No yang akan melakukan pembayaran kasbon")
    
    no_id = input("No: ")
    no = int(no_id) - 1
    os.system('clear')
    print(f"""
Dipilih
Nama           : {data_kasbon[no][1]} 
Total saat ini : {data_kasbon[no][2]}
    """)
    nominal_saat_ini = data_kasbon[no][2]
    
    tambah_nominal = int(input("nominal kasbon yang dibayar: "))
    nominal_baru = nominal_saat_ini - tambah_nominal

    if nominal_baru > 0:
        sql = "UPDATE kasbon SET total_kasbon=%s WHERE id=%s"
        val = (nominal_baru, data_kasbon[no][0],)
        cursor.execute(sql, val)
        
    else:
        sql = "DELETE FROM kasbon where id=%s"
        val = (data_kasbon[no][0],)
        cursor.execute(sql, val)
        print("Kasbon lunas!")
        
    db.commit()

    print(f"Data Nominal sukses dibayar : {cursor.rowcount}")
    
def tambah_kasbon(db):
    cursor = db.cursor()
    show_data(db)
    sql_id = "SELECT * FROM kasbon"
    cursor.execute(sql_id)
    result = cursor.fetchall()
    
    data_kasbon = []
    # totals = []
    for data in result:
        data = list(data)
        # total = list(total)
        data_kasbon.append(data) 
        # totals.append(total)
    
    print("\n\n\n\nPilih No yang akan ditambah kasbon")
    
    no_id = input("No: ")
    no = int(no_id) - 1
    os.system('clear')
    print(f"""
Dipilih
Nama           : {data_kasbon[no][1]} 
Total saat ini : {data_kasbon[no][2]}
    """)
    nominal_saat_ini = data_kasbon[no][2]
    
    tambah_nominal = int(input("Tambah nominal kasbon: "))
    nominal_baru = nominal_saat_ini + tambah_nominal

    sql_update = "UPDATE kasbon SET total_kasbon=%s WHERE id=%s"
    val = (nominal_baru, data_kasbon[no][0],)
    cursor.execute(sql_update, val)
    db.commit()
    print(f"Data Nominal sukses ditambah : {cursor.rowcount}")


    # jum_kasbon = input("Masukkan jumlah kasbon: ")



if __name__=="__main__":
    os.system('clear')
    menu()
    while True:
        
        print("""\n\n\n
------------+
1. Home     |
2. Keluar   |
------------+
    """)
        pilih = input("Pilih: ")
        if pilih == "1":
            os.system('clear')
            menu()
        elif pilih == "2":
            print("Terimakasih telah menggunakan aplikasi ini")
            sys.exit()
        else:
            print("input tidak valid")
            
    
    
