from all_function import *

with open('user.csv', mode ='r') as file_user:
    user = read(file_user) 

def login(data):
    username = input("Masukkan username: ")
    for i in range (1, len (data)):
        if username == data [i][1]:
            password = input("Masukkan password: ")
            if password == data [i][2]:
                print(f"Selamat datang {data[i][3]} {data[i][1]}")
                return username
            else:
                print("Password salah")
        else:
            print("Username tidak terdaftar")

# Aplikasi pada main.py

# from src.F02 import *
# login_id = login(user) # login_id dipakai sebagai variabel global di main.py untuk menentukan kepemilikan item, akses fungsi tertentu, dan status login user          
