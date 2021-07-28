# DirectSend - usage manual
Direct send is a fast and secure tool to transfer big files without any fees, as there is no server in the middle of the operation. The application uses a TCP socket to transfer all types of files directly from the sender to the receiver. The disadvantage is that the receiver has to have port forwarding set up, witch is a bit complicated for the general user.
<br> <br>
## Prepare to transfer

### 1. Set up port forwarding on the receiver's end
If you are not familiared with port forwarding, here is a useful blog post that will help you set it up: <br>
https://www.lifewire.com/how-to-port-forward-4163829

**Here are the settings required for this application:**  <br>
Protocol: TCP  <br>
Port: 10553  <br>
Internal IP: <receiver machine's local ip> <br> <br>

### 2. Get and set up receiver key file
To prepare for a transfer, the user that is receiving the file(s) has to send the sender the **rcvkey.ini** file generated automatically on the receiver app launch and saved on the same directory as the app. The sender should put that file in the sender app's working directory in order for it to be read. If the file is detected succesfully, the operation will proceed normally.
 
