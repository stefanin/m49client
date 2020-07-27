**M49Client:**

   Windows:

    Install the pyinstaller:

        pip install pyinstaller

    Create the M49Cient.exe:

            pyinstaller.exe -F .\M49Client.py

    Copy the M49Client.exe to M49 download directory     



   Mac:

   Linux:

   Release :
    
    2020 06 27 first release


   
   **TOOLS**

    fileTosyslog.py:
        send the file lines to a syslog server, it wait the file updates that will send to the syslog server. 
         
               fileTosyslog SYSLOGSERVERIP UDPPORT(514) FILE SWITCH

    Release :
    
    2020.07.27 add SWITCH -E ERROR -W WARN
    2020.06.27 first release

