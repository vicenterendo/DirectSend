import socket
import os
from time import sleep
from cryptography.fernet import Fernet
from tqdm import tqdm
from math import ceil

os.system("cls")

print("=======================")
print(f"[*] Reading sender key...")

while True:
      try:
            with open('rcvkey.ini', 'rb') as file:
                  recvcode = file.read()
            break
      except:

            lr = [5, 4, 3, 2, 1]

            print("=======================")
            os.system('cls') 
            for c in range(0, 5):
                  os.system('color c')
                  print("=======================")
                  print(f"[*] No key found")
                  print("=======================")
                  sleep(0.3)
                  os.system('cls')
                  os.system('color 7')
                  
                  
                  sleep(0.3)


            for c in lr:
                  os.system('cls')
                  os.system('color c')
                  print(f"[*] Error while trying to find key, please drag the key file to the same folder as the app. \n[<->] Trying again in {c} seconds...")
                  sleep(1)
            
            if 'rcvkey.ini' in os.listdir():
                  os.system('color 2')
                  os.system('cls')
                  lr = [2, 1]
                  for c in lr:
                        print("=======================")
                        print(f"[*] Key was found! \n------\n[<->] Continuing in {c} seconds...")
                        print("=======================")
                        sleep(1)
                        os.system('cls')
                  os.system('cls')
                  os.system('color f')
os.system('cls')
#os.system('color f1')
ipdecoder = Fernet(b'xX3-smiN-dItnevmRZ50PhwO9DLqwDmvGo7VXG7GsF4=')

ipaddr = ipdecoder.decrypt(recvcode)


print("=======================")
print(f"[/] Establishing connection...")
currentthreads = {}
runcommand = ""


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((str(ipaddr).strip("'b").strip("'").strip('"'), 10553))

print("=======================")
print(f"[+] Connected to Vizzeer's PC!")


print("=======================")
path = input(f"[*] Please insert file path --> ")


print("=======================")
filename = input(f"[*] What name should the file have on the receiver's PC? --> ")
client.send(filename.encode('utf-8'))


print("=======================")


filetransfer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
filetransfer.connect(((ipaddr, 10554)))

done = 0

with open(path, 'rb') as file:
      image_data = file.read(2048)
      file_size = os.path.getsize(path)
      client.send(str(file_size).encode('utf-16'))
      count = 0
      pbar = tqdm(total=int(file_size), desc='Sending file', unit=' bytes')
      while image_data:
            filetransfer.send(image_data)
            if count <= int(file_size):
                  pbar.update(2048)
                  count =+ 2048
            image_data = file.read(2048)
            sleep(0.00009)


print("=======================")
print(f"[*] Saving file...")

filetransfer.close()
client.close()

print("=======================")
print(f"[!] Data saved succesfully, exiting in 10 seconds...")

sleep(10)