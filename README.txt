Product Scanner

\\\******************************************************************\\\

Step-1 ( Enabling Network Discovery and Samba in WIndows)

Enable Network Discovery in Widows
1.Go to network and turn on Network Discovery

2.Control panel-> Programs -> Programs and features ->Turn Windows features -> Search and enable SMB 1.0/CIFS File Sharing Support..

3.Control panel -. Administartor tools -> Services ( to turn on the services)
   a.Navigate to  Standard Tab
   b.Scroll down and find DNS client and make sure it is running
   c.Find 'Function Discovery Resource Publisher' and start the service and change start up type to 'Automatic'
   d.Find 'SSCP Discovery and do same as above
   e.Find UpnP service and do the same

3.Reboot the System


\\\******************************************************************\\\
Step -2 ( Installing and configuring SAMBA in Controller)

Open Terminal and run
----------------------------------------- 
sudo apt update 
sudo apt instal samba
-----------------------------------------

You can check whether is installed succesfully by running the below given command

-----------------------------------------
whereis samba
-----------------------------------------

Lets setup and configure samba

---------------------------------------
mkdir /home/<username>/sambashare/
---------------------------------------

The above command creates new folder sambashare in home directory.

Editing Configuration File

-------------------------------------
sudo nano /etc/samba/smb.conf
------------------------------------

Go to the end and type

------------------------------------
[sambashare]
    comment = Samba on Ubuntu
    path = /home/username/sambashare
    read only = no
    browsable = yes
-------------------------------------

press cltrl + O ( for save) and ctrl+X ( close)


Restart the samba service
----------------------------------------
sudo service smbd restart
----------------------------------------

Set up an account
----------------------------------------
sudo smbpasswd -a username
----------------------------------------

Thats it..!! 


\\\******************************************************************\\\


Step -3 

Run device_scanner.py

