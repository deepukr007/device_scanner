import socket
import os
os.system('net view > conn.tmp')
f = open('conn.tmp', 'r')
f.readline();f.readline();f.readline()

device_common_name = "Dee"   //Enter common names of your devices

conn = []
host_ip=[]
host = f.readline()
while host[0] == '\\':
    conn.append(host[2:host.find(' ')])
    host = f.readline()

print (conn ,'\n\n\n')
f.close()

conn = [ x for x in conn if not x.find(device_common_name)]



def get_Host_name_IP(): 
    try:
        for i in conn:
          host_ip.append(socket.gethostbyname(i) ) 
    except: 
        print("Unable to get IP for " , i) 
  
# Driver code 
get_Host_name_IP() 

print ('Name \t\t\t  IP Address')
for n,g in zip(conn,host_ip):
    print (n + '\t\t\t' + g)


if(input()):
  print('<DeviceScannner/>')
