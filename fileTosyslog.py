RELEASE="2020.08.27"
import os
import time
import logging
import logging.handlers
import socket
import sys

M49logger = logging.getLogger('M49Logger')
M49logger.setLevel(logging.INFO)
hostname = socket.gethostname()

fileSeek=0
fileStatus=0
conta=0
fileStatuslast=0
def leggefiletosyslog(fileName,fileSeek,M49logger,ERROR=False,WARN=False):
        try:
            FULL=True
            f = open(fileName, "r")
            f.seek(fileSeek)# posizione precedente
            with f as l:
                content=f.read().splitlines()
                fileSeek=f.tell()
            f.close()
            #print(fileSeek)
            conta =0
            for riga in content:
                if "ERROR" in riga:
                    if ERROR==True:
                        print(hostname,"#",riga)
                        M49logger.info(hostname+"#"+riga)
                        conta+=1
                        FULL=False    
                if "WARN" in riga:
                    if WARN==True:
                        print(hostname,"#",riga)
                        M49logger.info(hostname+"#"+riga)
                        conta+=1
                        FULL=False    
                if FULL==True:    
                    M49logger.info(hostname+"#"+riga)
                    conta+=1
            print(conta," messaggi")
        except:
            print("Errore file ",fileName)
            M49logger.info(hostname+"#"+"Errore file "+fileName)
        return fileSeek

WARN=False
ERROR=False
if '-E' in sys.argv:
    ERROR=True
    print('Print and send to syslog ERROR messages')
if '-W' in sys.argv:
    WARN=True
    print('Print and send to syslog WARN messages')

try:
    handler = logging.handlers.SysLogHandler(address = (sys.argv[1],int(sys.argv[2])))
    M49logger.addHandler(handler)
    fileName=sys.argv[3]
    while True:
        print("Verifico i file")
        try:
            fileStatus=os.stat(fileName).st_size
            #print(fileStatus)
            if (fileStatus>fileStatuslast): #file incrementato
                    fileStatuslast=leggefiletosyslog(fileName,fileStatuslast,M49logger,ERROR,WARN)
            conta+=1
        except:
            print("Errore file ",fileName)
            M49logger.info(hostname+"#"+"Errore file "+fileName)

        print("Ho finito n°: ",conta)
        time.sleep(20)

except:
    print ("fileTosyslog "+RELEASE)
    print("!mmmm, fileTosyslog SYSLOGSERVERIP UDPPORT(514) FILE SWITCH")
    print("additional SWITCH:")
    print("    -E Print and send to syslog ERROR messages")
    print("    -W Print and send to syslog WARN messages")
