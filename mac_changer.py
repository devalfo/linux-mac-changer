#!/usr/bin/env python
'''
this tool is make by devalfo and marouan you can contact us for any updates or proposition
if u updated or changed the tool give us credit dont be a script kiddie
devalfo github:https://github.com/devalfo
'''
import subprocess
print("""             
                                                ,,                                                          
                                              `7MM                                                          
                                                MM                                                          
`7MMpMMMb.pMMMb.   ,6"Yb.  ,p6"bo       ,p6"bo  MMpMMMb.   ,6"Yb.  `7MMpMMMb.  .P"Ybmmm .gP"Ya `7Mb,od8     
  MM    MM    MM  8)   MM 6M'  OO      6M'  OO  MM    MM  8)   MM    MM    MM :MI  I8  ,M'   Yb  MM' "'     
  MM    MM    MM   ,pm9MM 8M           8M       MM    MM   ,pm9MM    MM    MM  WmmmP"  8M""""""  MM         
  MM    MM    MM  8M   MM YM.    ,     YM.    , MM    MM  8M   MM    MM    MM 8M       YM.    ,  MM         
.JMML  JMML  JMML.`Moo9^Yo.YMbmd'       YMbmd'.JMML  JMML.`Moo9^Yo..JMML  JMML.YMMMMMb  `Mbmmd'.JMML.       
                                                                              6'     dP                     
                                                                              Ybmmmd'              linux
                                                                                                  (version 1.1)
                                                                                                  ==by devalfo==
""")
print ("MAC Address Changer allows you to change (spoof) Media Access Control (MAC) Address of your Network Interface Card (NIC) instantly. It has a very simple user interface and provides ample information regarding each NIC in the machine. Every NIC has a MAC address hard coded in its circuit by the manufacturer.")
print("")
print("")
print("")
print("Your curent mac adress is : ")
subprocess.call("cat /sys/class/net/eth0/address", shell=True)
print("")
print("")
print("")
print("[1]-Dell computers")
print ("[2]-Apple laptop")
print("[3]-Huwawei phone")
print("[4]-Samsung android phone")
print("[5]-IPhone")
print("[6]-Playstation 4")
print("[7]-xiaomi phone")
print("[8]-Ipod")
print("[9]-HP Printer")
print("[10]-Samsung TV")
print("[11]-Custum mac changer")
dnp=input("What do you want :")
print(dnp)
if(dnp == 1):
    dellcomputer="18:03:73:E9:FB:86"
    subprocess.call("ifconfig wlan0 down",shell=True)
    subprocess.call("ifconfig wlan0 hw ether " + dellcomputer, shell=True)
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ dellcomputer, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")

    print("your new mac adress is : " + dellcomputer)
elif(dnp == 2):
    applelaptop=" 00:1F:5B:C7:EE:2F"

    subprocess.call("ifconfig wlan0 down" ,shell=True)
    subprocess.call("ifconfig wlan0 hw ether " + applelaptop, shell=True)
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ applelaptop, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + applelaptop)
elif(dnp == 3):
    huwawei="8C:EB:C6:15:43:A4"

    subprocess.call("ifconfig wlan0 down ",shell=True) #hada hwawhi phone
    subprocess.call("ifconfig wlan0 hw ether " +huwawei, shell=True)
    subprocess.call("ifconfig  wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ huwawei, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + huwawei)
elif(dnp == 4):
    samsung=" 8C:F5:A3:CB:14:C6"

    subprocess.call("ifconfig wlan0 down",shell=True) #samsung android phone
    subprocess.call("ifconfig wlan0 hw ether " +samsung, shell=True)
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ samsung, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + samsung)
elif(dnp == 5):
    iphone=" 28:A0:2B:EC:6F:93"

    subprocess.call("ifconfig wlan0 down",shell=True)
    subprocess.call("ifconfig wlan0 hw ether " + iphone, shell=True) #mhm hada iphone
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ iphone, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + iphone)
elif(dnp == 6):
    playstation4=" F8:46:1C:0D:27:1B"

    subprocess.call("ifconfig wlan0 down" ,shell=True)
    subprocess.call("ifconfig wlan0 hw ether "+ playstation4, shell=True) #playstation 4
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ playstation4, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + playstation4)
elif(dnp == 7):
    xiaomi="EC:D0:9F:82:EE:3F "

    subprocess.call("ifconfig wlan0 down" ,shell=True)
    subprocess.call("ifconfig wlan0 hw ether "+ xiaomi, shell=True) #xiaomi
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ xiaomi, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + xiaomi)
elif(dnp == 8):
    ipod="FC:D8:48:03:54:8C"

    subprocess.call("ifconfig wlan0 down" ,shell=True)
    subprocess.call("ifconfig wlan0 hw ether "+ ipod, shell=True) #ipod
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ ipod, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + ipod)
elif (dnp == 9):
    hpprinter = "D8:9D:67:DA:2F:32"

    subprocess.call("ifconfig wlan0 down", shell=True)
    subprocess.call("ifconfig wlan0 hw ether " + hpprinter, shell=True)  # hpprinter
    subprocess.call("ifconfig wlan0 up", shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ hpprinter, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + hpprinter)
elif(dnp == 10):
    samsungtv="F8:77:B8:0C:49:B1"

    subprocess.call("ifconfig wlan0 down" ,shell=True)
    subprocess.call("ifconfig wlan0 hw ether "+ samsungtv, shell=True) #xiaomi
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ samsungtv, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("your new mac adress is : " + samsungtv)


#had linput dial lcustum mac dir li bghity
elif(dnp == 11):
    frp=input("type the custum mac adress (like 00:11:22:33:44:55): ")

    subprocess.call("ifconfig wlan0 down",shell=True)
    subprocess.call("ifconfig wlan0 hw ether " + frp , shell=True)
    subprocess.call("ifconfig wlan0 up",shell=True)
    subprocess.call("ifconfig eth0 down" ,shell=True)
    subprocess.call("ifconfig eth0 hw ether "+ frp, shell=True) #xiaomi
    subprocess.call("ifconfig eth0 up",shell=True)
    subprocess.call("service network-manager restart",shell=True)
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("[-]The mac adress is changin..")
    print("The mac adress is : " + frp)

else:
    print("this choise isn't right")
    print("restart the script")
    '''
    thank you for using my first python script
    i apreseate this thank you 
    '''

