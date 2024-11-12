import qrcode as qr
import os

os.system("pip install Pillow qrcode")

def qr_code_creator():
    try:
        user = input("[+] Enter input to create QR: ")
        qr_code_save = input("[+] Enter Filename to save QR: ")
        path = input("[+] Enter Path to save QR_Code (Ex:- C:/user OR just press Enter): ")
        qr_code = qr.make(user)
        qr_code.save(path+"/"+qr_code_save+".png")
        print()
        print('[+] File Created Successfully')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    try:
        while True:
            print()
            ch = int(input("[+] Enter 1 to create QR_Code OR 2 to exit: "))
            if ch == 1:
                qr_code_creator()

            elif ch == 2:
                print()
                print('[+] Exiting...')
                break
    except Exception as e:
        print(str(e))
