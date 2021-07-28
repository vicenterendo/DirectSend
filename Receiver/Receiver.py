import socket
import os
import threading
from pynput.keyboard import Key, Controller
from time import sleep
from cryptography.fernet import Fernet
import requests
from tqdm import tqdm
from math import ceil
import sys

os.system("cls")


ipaddr = requests.get('https://api.ipify.org').text
ipencoder = Fernet('xX3-smiN-dItnevmRZ50PhwO9DLqwDmvGo7VXG7GsF4='.encode())
code = ipencoder.encrypt(ipaddr.encode())


with open('rcvkey.ini', 'wb') as file:
      file.write(code)

print("=======================")
print("[*] Reciever key has been writen to rcvkey.ini ")


print("=======================")
print(f"[/] Waiting for connection...")
currentthreads = {}
runcommand = ""



while True:
      try:
            adreslist = []
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('192.168.1.120', 10553))
            server.listen()
            client, address = server.accept()



            print("=======================")
            print(f"[+] Connected to {address[0]}:{address[1]}")

            



            """code = ""

            partcount = client.recv(1024).decode('utf-8')
            for lap in range(0, int(partcount)+2):
                  code = code + client.recv(1024)"""
            

            print("=======================")
            filename = str(input("File path: "))


            print("=======================")
            print(f"[*] Selected filename {filename}")

            
            
            print("=======================")
            print(f"[*] File content received")
            with open(f"{filename}", "wb") as file:
                  ft = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  ft.bind(('192.168.1.120', 10554))
                  ft.listen()
                  ftc, ftca = ft.accept()
                  file_size = client.recv(1024).decode('utf-16')
                  
                  code = ""
                  count = 0

                  print(file_size)

                  with open(filename, "wb") as file:
                        pbar = tqdm(total=int(file_size), desc='Donwloading file', unit=' bytes')
                        file_part = ftc.recv(2048)
                        pbar.update(sys.getsizeof(file_part))
                        while file_part:
                              file.write(file_part)
                              if count <= int(file_size):
                                    pbar.update(sys.getsizeof(file_part))
                                    count =+ sys.getsizeof(file_part)
                              file_part = ftc.recv(2048)


                  ftc.close()
                  


                  print("\n=======================")
                  print(f"[!] Data saved succesfully")
                  print("=======================")

                  client.close()
                  print(f"\n[-] Connection closed, waiting for another connection...")
      except:
            client.close()
            print(f"[-] Connection closed, waiting for another connection...")