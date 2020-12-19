'''
    Generate qr codes using Python
'''
from png import main
import pyqrcode


def generate_qr():
    qr = pyqrcode.create(input("Enter string to generate qr for: "))
    filename=input("Enter a filename to store your qr: ")
    qr.png(filename+'.png',scale=10)
    print("QR successfully generated.")

if __name__ == "__main__":
    generate_qr()