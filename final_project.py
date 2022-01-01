import smtplib
import getpass
from email.message import EmailMessage #import class EmailMessage agar lebih cleanly

def emailTujuan():
    jumlahEmailTujuan = int(input("Masukan jumlah email penerima : "))
    def tambahEmail ():
        file = open ("receiver_list.txt",'a')
        file.write('\n')
        file.write(input("Masukan email tujuan : "))
        file.close()
    for x in range (jumlahEmailTujuan):
        tambahEmail()
    print()
    print('-------------------------------')
    print ('Daftar email : ')
    f = open ("receiver_list.txt",'r')
    print(f.read())
    print('-------------------------------')

def kirimEmail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.ehlo()

    kontak = []
    #untuk memasukan isi file kedalam list tanpa \n terbaca
    with open ("receiver_list.txt") as f:
        kontak = f.read().splitlines() 

    # mengirim email
    msg = EmailMessage() #membuat objek msg
    msg['Subject'] = input("Masukan Subject email : ")
    msg['From'] = emailPengirim
    msg['To'] = kontak
    body = input("Masukan Body email : ")
    msg.set_content(body)

    fileLampiran = input("Masukan nama file yang akan dilampirkan beserta type file nya: ")
    print ('Lampiran berhasil di upload')

    with open (fileLampiran, 'rb') as l: #memanggil file lampiran dan diharuskan dalam satu direktori dengan file python
        file_data = l.read() 
        file_name = l.name
    
    msg.add_attachment(file_data, maintype = 'application', subtype='octet-stream', filename = file_name) #maintype = application untuk mengeneralisir semua jenis file, 
    smtp.login(emailPengirim, passwordEmail)
    smtp.send_message(msg)
    smtp.quit()
    print ('Email berhasil dikirim :)')
    print()
    print('-------------------------------')


while True :
    print ("----- Final Project -----")
    print ("1. Masukan Email & Password Pengirim")
    print ("2. Masukan Email tujuan")
    print ("3. Kirim Email")
    print ("4. Keluar")
    pilihan = int (input("Masukan pilihan anda : "))

    if pilihan == 1 :
        emailPengirim = input("Masukan email pengirim : ")
        passwordEmail = getpass.getpass("Masukan passowrd email : ")
        print ('Email pengirim berhasil disimpan')
        print('-------------------------------')
        print()

    elif pilihan == 2 :
        emailTujuan()
        print('-------------------------------')
        print()
    
    elif pilihan == 3 :
        kirimEmail()
        print('-------------------------------')
        print()
    elif pilihan == 4 :
        print ('Terima kasih :)')
        print()
        print('-------------------------------')
        break
    else :
        print ("Inputan tidak tersedia")
    

        








