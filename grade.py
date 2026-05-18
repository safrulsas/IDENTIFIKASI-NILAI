from libs import welcome_message

nama = {
    
}
def tambah_nama(siswa, nilai):
    nama[siswa] = nilai
    
tambah_siswa = None
tambah_siswa = int(input("ingin menambah berapa siswa? : "))
for i in range(tambah_siswa):
    def tambah_nama(siswa, nilai):
        nama[siswa] = nilai
    

    tambah_nama(siswa=input("Masukkan nama anda : "), nilai = int(input('masukkan nilai : ')))

def nomor_1():
    for key in nama.keys():
        print(key)
    print('''
    1. Nama siswa      
    2. Nilai siswa
    3. Nama dan nilai siswa
    4. Tier siswa
    5. keluar''')
    pilih = int(input('pilih nomor : '))    

def nomor_2():
    for value in nama.values():
        print(value)
    print('''
    1. Nama siswa      
    2. Nilai siswa
    3. Nama dan nilai siswa
    4. Tier siswa
    5. keluar''')
    pilih = int(input('pilih nomor : '))
    
def nomor_3():
    for key, value in nama.items():
        print(f'{key} : {value}')
        print('''
    1. Nama siswa      
    2. Nilai siswa
    3. Nama dan nilai siswa
    4. Tier siswa
    5. keluar''')
    pilih = int(input('pilih nomor : '))

def nomor_4():
    for value, key in nama.items():
        if value >= 85 and value <= 100:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : A \n Penentuan : Lulus \n Kesan : Keren!!, anda lulus dengan nilai diatas rata rata')
        elif value >= 71 and value <= 84:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : B \n Penentuan : Lulus \n Kesan : bagus, tapi perlu ditingkatkan')
        elif value <= 70 and value >= 60:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : C \n Penentuan : Tidak lulus \n Kesan : jangan berkecil hati, masih ada tahun depan')
        else:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : D \n Penentuan : Tidak lulus \n Kesan : Nilainya cukup kurang, belajarnya tolong ditingkatkan lagi')
    print('''
    1. Nama siswa      
    2. Nilai siswa
    3. Nama dan nilai siswa
    4. Tier siswa
    5. keluar''')
    pilih = int(input('pilih nomor : '))
    

welcome_message('IDENTIFIKASI NILAI')
print('''
    1. Nama siswa      
    2. Nilai siswa
    3. Nama dan nilai siswa
    4. Tier siswa
    5. keluar''')
pilih = int(input('pilih nomor : '))
style = "=" * (len(nama) + 35)

if pilih == 1:
    nomor_1()

elif pilih == 2:
    nomor_2()
    
elif pilih == 3:
    nomor_3()
    
elif pilih == 4:
    for value, key in nama.items():
        if value >= 85 and value <= 100:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : A \n Penentuan : Lulus \n Kesan : Keren!!, anda lulus dengan nilai diatas rata rata')
        elif value >= 71 and value <= 84:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : B \n Penentuan : Lulus \n Kesan : bagus, tapi perlu ditingkatkan')
        elif value <= 70 and value >= 60:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : C \n Penentuan : Tidak lulus \n Kesan : jangan berkecil hati, masih ada tahun depan')
        else:
            print(style)
            print(f' Nama : {key} \n Nilai : {value} \n Tier : D \n Penentuan : Tidak lulus \n Kesan : Nilainya cukup kurang, belajarnya tolong ditingkatkan lagi')
    
elif pilih == 5:
    print('terimakasih telah memakai program kami')
    quit
    
else :
    print('nomor yang anda input tidak valid')