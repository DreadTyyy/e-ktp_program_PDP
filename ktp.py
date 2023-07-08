import json
import datetime
file_path = "dataBases_list.json"

def menu():
    print("="*100)
    print("SELAMAT DATANG DI PROGRAM E-KTP\n")
    print("Daftar Menu:\n[1] Sign E-KTP\n[2] Search E-KTP\n[9] Quit Program")
    pilihan = int(input("pilihan >> "))
    pil_menu(pilihan);

def pil_menu(pil):
    if pil == 1:
        sign();
    elif pil == 2:
        search();
    elif pil == 9:
        print("\nQUIT PROGRAM E-KTP");
    else:
        call_back();

def call_in():
    print("\nIngin menjelajah lagi?")
    print("[0] Ya\n[9] Tidak")
    pilihan = int(input("pilihan >> "))
    call_in_pil(pilihan);

def call_in_pil(pil):
    if pil == 0:
        menu();
    elif pil == 9:
        print("QUIT PROGRAM");

def call_back():
    print("\nERROR INPUT")
    print("[0] Back\n[9] Quit")
    pilihan = int(input("pilihan >> "))
    call_in_pil(pilihan);

#----------SIGN Menu-------------------
def sign():
    global file_path
    waktu = datetime.date.today()
    year = waktu.year
    print("Memasuki proses pembuatan E-KTP")
    print("Masukkan data diri anda\n")
    nik = int(input("NIK : "))
    nik_data = nik
    digit = len(str(nik))
    while(digit!=16):
        print("NIK harus berjumlah 16 digit, masukkan ulang")
        nik = int(input("NIK : "))
        nik_data = nik
        digit = len(str(nik));
    
    nama = str(input("Nama Lengkap : "))
    nama_data = nama;

    tempat_lahir = str(input("Tempat Lahir : "))
    tempat_lahir_upper = tempat_lahir.upper()
    
    tanggal_lahir = int(input("Tanggal Lahir : "))
    bulan_lahir = int(input("Bulan Lahir(angka) : "))
    while(bulan_lahir < 1 or bulan_lahir > 12):
        print("Bulan yang anda masukkan salah, masukkan ulang!")
        bulan_lahir = int(input("Bulan Lahir(angka) : "))
    tahun_lahir = int(input("Tahun Lahir(XXXX) : "))
    range_th_lahir = year - tahun_lahir
    while(range_th_lahir < 17):
        print("Pembuatan E-KTP gagal, minimal usia 17 tahun!")
        print("[1] Masukkan ulang\n[9] Quit")
        pilihan = int(input("pilihan >> "))
        if pilihan == 1:
            tahun_lahir = int(input("Tahun Lahir(XXXX) : "))
            range_th_lahir = year - tahun_lahir
        elif pilihan == 9:
            print("Quit laman")
            return
        else:
            call_back()
            return
    ttl = tempat_lahir_upper + ", " + str(tanggal_lahir) + "-" + str(bulan_lahir) + "-" + str(tahun_lahir)
    ttl_data = ttl

    while True:
        print("Jenis Kelamin : \n[1] Laki-Laki\n[2] Perempuan")
        pilihan = int(input("Pilihan >> "))
        if pilihan == 1:
            jenis_kelamin = "LAKI-LAKI"
            break
        elif pilihan == 2:
            jenis_kelamin = "PEREMPUAN"
            break
        print("ERROR input//Masukkan ulang!");
    jenis_kelamin_data = jenis_kelamin

    while True:
        gol_darah_pil = str(input("Golongan Darah : "))
        if gol_darah_pil in["a","A"]:
            golongan_darah = "A"
            break
        elif gol_darah_pil in["b","B"]:
            golongan_darah = "B"
            break
        elif gol_darah_pil in["c","C"]:
            golongan_darah = "C"
            break
        elif gol_darah_pil in["ab","AB","aB","Ab"]:
            golongan_darah = "AB"
            break
        print("Golongan darah tidak ditemukan//Masukkan ulang!")
    golongan_darah_data = golongan_darah

    provinsi = str(input("Provinsi : "))
    provinsi_data = provinsi

    while True:
        print("[1] Kabupaten\n[2] Kota")
        pilihan = int(input("Pilihan >> "))
        if pilihan == 1:
            kab = "KABUPATEN"
            nama_kabupaten = str(input("Kabupaten : "))
            break
        if pilihan == 2:
            kab = "KOTA"
            nama_kabupaten = str(input("Kota : "))
            break
        print("ERROR input//Masukkan ulang!")
    kabupaten_data = nama_kabupaten
    kecamatan = str(input("Kecamatan : "))
    kecamatan_data = kecamatan
    kelurahan = str(input("Kelurahan : "))
    kelurahan_data = kelurahan
    while True:
        rt = int(input("RT(ANGKA) : "))
        range_rt = len(str(rt))
        rt_type = type(rt)
        rt_ = "" 
        for i in range(range_rt,3):
            rt_ = "0" + str(rt_)
        rt = rt_ + str(rt)
        if rt_type == type(0):
            break
        print("Masukkan data dalam angka!");
    while True:
        rw = int(input("RW(ANGKA) : "))
        range_rw = len(str(rw))
        rw_type = type(rw)
        rw_ = ""
        for i in range(range_rw,3):
            rw_ = "0" + str(rw_)
        rw = rw_ + str(rw)
        if rw_type == type(0):
            break
        print("Masukkan data dalam angka!");
    
    rtrw = rt + "/" + rw
    rtrw_data = rtrw
    alamat = str(input("Alamat : "))
    alamat_data = alamat

    while True:
        print("\nAgama : ")
        print("[1] ISLAM\n[2] KRISTEN\n[3] KATOLIK\n[4] HINDU\n[5] BUDDHA\n[6] KONGHUCU")
        pilihan = int(input("Pilihan >> "))
        if pilihan == 1:
            agama = "ISLAM"
            print("Data agama anda ISLAM")
            break;
        elif pilihan == 2:
            agama = "KRISTEN"
            print("Data agama anda KRISTEN")
            break;
        elif pilihan == 3:
            agama = "KATOLIK"
            print("Data agama anda KATOLIK")
            break;
        elif pilihan == 4:
            agama = "HINDU"
            print("Data agama anda HINDU")
            break;
        elif pilihan == 5:
            agama = "BUDDHA"
            print("Data agama anda BUDDHA")
            break;
        elif pilihan == 6:
            agama = "KONGHUCU"
            print("Data agama anda KONGHUCU")
            break;
        print("ERROR input//Masukkan ulang!");
    agama_data = agama

    while True:
        print("Status perkawinan : ")
        print("[1] Belum Kawin\n[2] Sudah Kawin")
        pilihan = int(input("Pilihan >> "))
        if pilihan == 1:
            status = "BELUM KAWIN"
            break;
        elif pilihan == 2:
            status = "SUDAH KAWIN"
            break;
        print("ERROR input//Masukkan ulang!")
    status_data = status

    pekerjaan = str(input("Pekerjaan : "))
    pekerjaan_data = pekerjaan

    while True:
        print("Kewarganegaraan : ")
        print("[1] WNI\n[2] WNA")
        pilihan = int(input("Pilihan >> "))
        if pilihan == 1:
            kewarganegaraan = "WNI"
            berlaku_hingga = "SEUMUR HIDUP"
            break;
        elif pilihan == 2:
            kw = str(input("Negara asal : "))
            kewarganegaraan = kw
            berlaku_hingga = str(tanggal_lahir) + "-" + str(bulan_lahir) + "-" + str(year+5)
            break
        print("ERROR input//Masukkan ulang!")
    kewarganegaraan_data = kewarganegaraan
    
    #OUTPUT E-KTP
    print("-"*100)
    provinsi = f"PROVINSI {provinsi.upper()}"
    range_provinsi = int(len(provinsi))
    while True:
        if range_provinsi%2 == 0:
            space = " "*int((98-range_provinsi)/2)
            break
        if range_provinsi%2 != 0:
            provinsi = f"{provinsi} "
            range_provinsi = int(len(provinsi))
            space = " "*int((98-range_provinsi)/2)
            break;
    print(f"|{space}{provinsi}{space}|")
    nama_kabupaten = f"{kab} {nama_kabupaten.upper()}"
    range_kabupaten = int(len(nama_kabupaten))
    while True:
        if range_kabupaten%2 == 0:
            space = " "*int((98-range_kabupaten)/2)
            break
        if range_kabupaten%2 != 0:
            nama_kabupaten = f"{nama_kabupaten} "
            range_kabupaten = int(len(nama_kabupaten))
            space = " "*int((98-range_kabupaten)/2)
            break;
    print(f"|{space}{nama_kabupaten}{space}|")
    print("|" + " "*98 + "|")
    nik = f"|   NIK             : {nik}"
    space = " "*(99-int(len(nik)))
    print(f"{nik}{space}|")
    nama = f"|   Nama              : {nama.upper()}"
    space = " "*(99-int(len(nama)))
    print(f"{nama}{space}|")
    ttl = f"|   Tempat/TglLahir   : {ttl}"
    space = " "*(99-int(len(ttl)))
    print(f"{ttl}{space}|")
    jenis_kelamin = f"|   Jenis Kelamin     : {jenis_kelamin}"
    golongan_darah = f"Gol. Darah   : {golongan_darah}" 
    space_jK = " "*(50-int(len(jenis_kelamin)))
    jK_gD = f"{jenis_kelamin}{space_jK}{golongan_darah}"
    space_gD = " "*(99-int(len(jK_gD)))
    print(f"{jK_gD}{space_gD}|")
    alamat = f"|   Alamat            : {alamat.upper()}"
    space = " "*(99-int(len(alamat)))
    print(f"{alamat}{space}|")
    rtrw = f"|        RT/RW        : {rtrw}"
    space = " "*(99-int(len(rtrw)))
    print(f"{rtrw}{space}|")
    kelurahan = f"|        Kel/Desa     : {kelurahan.upper()}"
    space = " "*(99-int(len(kelurahan)))
    print(f"{kelurahan}{space}|")
    kecamatan = f"|        Kecamatan    : {kecamatan.upper()}"
    space = " "*(99-int(len(kecamatan)))
    print(f"{kecamatan}{space}|")
    agama = f"|   Agama             : {agama}"
    space = " "*(99-int(len(agama)))
    print(f"{agama}{space}|")
    status = f"|   Status Perkawinan : {status}"
    space = " "*(99-int(len(status)))
    print(f"{status}{space}|")
    pekerjaan = f"|   Pekerjaan         : {pekerjaan.upper()}"
    space = " "*(99-int(len(pekerjaan)))
    print(f"{pekerjaan}{space}|")
    kewarganegaraan = f"|   Kewarganegaraan   : {kewarganegaraan}"
    space = " "*(99-int(len(kewarganegaraan)))
    print(f"{kewarganegaraan}{space}|")
    berlaku_hingga = f"|   Berlaku Hingga    : {berlaku_hingga}"
    space = " "*(99-int(len(berlaku_hingga)))
    print(f"{berlaku_hingga}{space}|")        
    print("|" + " "*98 + "|")
    print("-"*100)    

    # Memasukkan data ke dictionary
    new_data = {
        "nik" : nik_data,
        "nama" : nama_data,
        "ttl" : ttl_data,
        "jenis kelamin" : jenis_kelamin_data,
        "golongan darah" : golongan_darah_data,
        "alamat" : alamat_data,
        "rtrw" : rtrw_data,
        "kelurahan" : kelurahan_data,
        "kecamatan" : kecamatan_data,
        "kabupaten" : kabupaten_data,
        "kabupaten/kota" : kab,
        "provinsi" : provinsi_data,
        "agama" : agama_data,
        "status perkawinan" : status_data,
        "pekerjaan" : pekerjaan_data,
        "kewarganegaraan" : kewarganegaraan_data,
        "berlaku hingga" : berlaku_hingga
    }
    def save_dataBases(data, file_path):
        try:
            with open(file_path, 'r') as file:
                found_data = json.load(file) # found data = isi file 
                print("proses...")
                print("="*100)
        except:
            found_data = []
        found_data.append(data) # new_data dimasukkan ke list found_data
        with open(file_path,"w") as file:
            json.dump(found_data,file)
    while True:
        try:
            save_dataBases(new_data, file_path)
            print("\nselamat data anda telah tersimpan")
            break
        except:
            print("\nERROR: data anda gagal tersimpan")
            break

    print("Tekan enter untuk keluar laman")
    input("")
    return menu()
#----------Search Menu--------------------
def search():
    global file_path
    list_data = 0
    while True:
        try:
            with open(file_path,"r") as file:
                databases = json.load(file)
                break
        except:
            print("Mohon maaf belum terdapat data di databases")
            print("Keluar laman...\n")
            return menu()
    print("\nMemasuki laman pencarian E-KTP")
    print("Cari data diri anda\n[1] Cari dengan NIK\n[2] Cari dengan Nama\n[9] Quit laman")
    pilihan = int(input("Pilihan >> "))
    if pilihan == 9:
        return menu()
    elif pilihan == 1:
        nik = str(input("\nMasukkan NIK anda : "))
        for data in databases:
            list_data+=1
            if str(data["nik"]) == str(nik):
                list_data-=1
                print("="*100)
                print("proses pencarian data...")
                break
            else:
                print(f"data dengan nik {nik} tidak ditemukan")
                print("Kembali ke laman")
                return search()
    elif pilihan == 2:
        nama = input("\nMasukkan nama anda : ")
        for data in databases:
            list_data+=1
            if data["nama"] == str(nama):
                list_data-=1
                print("="*100)
                print("proses pencarian data...")
                break
            else:
                print(f"data dengan nama {nama} tidak ditemukan")
                print("Kembali ke laman")
                return search()
    else:
        return call_back()    
    
    # inisialisasi data
    nik = databases[list_data].get("nik")
    nama = databases[list_data].get("nama")
    ttl = databases[list_data].get("ttl")
    jenis_kelamin = databases[list_data].get("jenis kelamin")
    golongan_darah = databases[list_data].get("golongan darah")
    alamat = databases[list_data].get("alamat")
    rtrw = databases[list_data].get("rtrw")
    kelurahan = databases[list_data].get("kelurahan")
    kecamatan = databases[list_data].get("kecamatan")
    nama_kabupaten = databases[list_data].get("kabupaten")
    kab = databases[list_data].get("kabupaten/kota")
    provinsi = databases[list_data].get("provinsi")
    agama = databases[list_data].get("agama")
    status = databases[list_data].get("status perkawinan")
    pekerjaan = databases[list_data].get("pekerjaan")
    kewarganegaraan = databases[list_data].get("kewarganegaraan")
    berlaku_hingga = databases[list_data].get("berlaku hingga")

    #OUTPUT E-KTP
    print("-"*100)
    provinsi = f"PROVINSI {provinsi.upper()}"
    range_provinsi = int(len(provinsi))
    while True:
        if range_provinsi%2 == 0:
            space = " "*int((98-range_provinsi)/2)
            break
        if range_provinsi%2 != 0:
            provinsi = f"{provinsi} "
            range_provinsi = int(len(provinsi))
            space = " "*int((98-range_provinsi)/2)
            break;
    print(f"|{space}{provinsi}{space}|")
    nama_kabupaten = f"{kab} {nama_kabupaten.upper()}"
    range_kabupaten = int(len(nama_kabupaten))
    while True:
        if range_kabupaten%2 == 0:
            space = " "*int((98-range_kabupaten)/2)
            break
        if range_kabupaten%2 != 0:
            nama_kabupaten = f"{nama_kabupaten} "
            range_kabupaten = int(len(nama_kabupaten))
            space = " "*int((98-range_kabupaten)/2)
            break;
    print(f"|{space}{nama_kabupaten}{space}|")
    print("|" + " "*98 + "|")
    nik = f"|   NIK             : {nik}"
    space = " "*(99-int(len(nik)))
    print(f"{nik}{space}|")
    nama = f"|   Nama              : {nama.upper()}"
    space = " "*(99-int(len(nama)))
    print(f"{nama}{space}|")
    ttl = f"|   Tempat/TglLahir   : {ttl}"
    space = " "*(99-int(len(ttl)))
    print(f"{ttl}{space}|")
    jenis_kelamin = f"|   Jenis Kelamin     : {jenis_kelamin}"
    golongan_darah = f"Gol. Darah   : {golongan_darah}" 
    space_jK = " "*(50-int(len(jenis_kelamin)))
    jK_gD = f"{jenis_kelamin}{space_jK}{golongan_darah}"
    space_gD = " "*(99-int(len(jK_gD)))
    print(f"{jK_gD}{space_gD}|")
    alamat = f"|   Alamat            : {alamat.upper()}"
    space = " "*(99-int(len(alamat)))
    print(f"{alamat}{space}|")
    rtrw = f"|        RT/RW        : {rtrw}"
    space = " "*(99-int(len(rtrw)))
    print(f"{rtrw}{space}|")
    kelurahan = f"|        Kel/Desa     : {kelurahan.upper()}"
    space = " "*(99-int(len(kelurahan)))
    print(f"{kelurahan}{space}|")
    kecamatan = f"|        Kecamatan    : {kecamatan.upper()}"
    space = " "*(99-int(len(kecamatan)))
    print(f"{kecamatan}{space}|")
    agama = f"|   Agama             : {agama}"
    space = " "*(99-int(len(agama)))
    print(f"{agama}{space}|")
    status = f"|   Status Perkawinan : {status}"
    space = " "*(99-int(len(status)))
    print(f"{status}{space}|")
    pekerjaan = f"|   Pekerjaan         : {pekerjaan.upper()}"
    space = " "*(99-int(len(pekerjaan)))
    print(f"{pekerjaan}{space}|")
    kewarganegaraan = f"|   Kewarganegaraan   : {kewarganegaraan}"
    space = " "*(99-int(len(kewarganegaraan)))
    print(f"{kewarganegaraan}{space}|")
    berlaku_hingga = f"|   Berlaku Hingga    : {berlaku_hingga}"
    space = " "*(99-int(len(berlaku_hingga)))
    print(f"{berlaku_hingga}{space}|")        
    print("|" + " "*98 + "|")
    print("-"*100)    

    print("Tekan enter untuk keluar laman")
    input("")
    return menu()   
menu()
    
        
    








    

    
