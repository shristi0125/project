import getpass
import os
import speech_recognition as sr
import pyttsx3
import time
import keyboard
import xml.etree.ElementTree as ET
os.system('tput setaf 4')
print("Enter The Required Password To Login")
x=getpass.getpass()

os.system("figlet MultiAutomation | lolcat")
os.system('sleep 2')
os.system('zenity --info --title "Python Automation" --width=400 --height=400 --text "CREATE PARTITION\n\nCONFIGURE DATANODE\n\nCONFIGURE NAMENODE\n\n\CREATE LVM PARTITION\n\nCONFIGURE AWS SERVICES\n\nSEE LINUX COMMANDS" ')
os.system('sleep 3')
print("===================welcome_To_MultiAutomation==================n")
os.system('sleep 1')
r = input("How Would You Like To Login as ?(Local/Remote):")
os.system('tput setaf 7')
while True:
    if r == "local":
        print(""" \n
        Press 1:  To See Date 
        Press 2:  To See Calendar 
        Press 3:  To See IP
        Press 4:  To See all the process running in the background
        Press 5:  To See how many time you open and close your os
        Press 6:  To See your RAM
        Press 7:  To See how much storage you used
        Press 8:  To check file size
        Press 9:  To See how many port were running in your os
        Press 10: To enter into root account
        Press 11: To install httpd service
        Press 12: To permanently  enable httpd service
        Press 13: TO EXIT""")
        ch =int(input("Enter your choice:"))
        print(ch)
        if ch ==1:
            os.system("date")
        elif ch==2:
            os.system('zenity --calendar') 
        elif ch==3:
            os.system('ifconfig enp0s3')
        elif ch==4:
            os.system("ps-aux")
        elif ch==5:
           os.system("uptime") 
        elif ch==6:
           os.system("free -m") 
        elif ch==7:
           os.system("df -h") 
        elif ch==8:
           os.system("ls -l -h") 
        elif ch==9:
           os.system("netstat -tnlp")
        elif ch==10:
           os.system("sudo su - root") 
        elif ch==11:
           os.system("yum install httpd") 
        elif ch ==12:
           os.system("systemctl enable httpd") 
        elif ch ==13:
           os.system("exit")

os.system('sleep 2')         
os.system("python3 sawan2.py")

pyttsx3.speak("welcome to hybrid automation")
print('say docker to start docker service')
print('say Partition to Create new partition')
print('say Hadoop to configure hadoop setup')
print('say LVM or Local Volume Management to to create LVM Partitions')
r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("start say...")
		audio = r.listen(source)
		print("speech done..")
		p = r.recognize_google(audio)
		print("you said..  " + p) 
		pyttsx3.speak("you says %s"%p)
		if(("Partition" in p) or ("partition" in p)) or (("create Partition for me" in p) or ("Create Partition For Me" in p)) :
			print("Input your device name : i.e. /dev/sdb")
			pyttsx3.speak("tell your device name")
			os.system("fdisk -l")
			x = input()
			pyttsx3.speak("you enter : " + x)
			print("are you sure your divece name is correct if yes the press 1")
			pyttsx3.speak("are you sure your divece name is correct if yes the press 1")
			print("say.. create partition")
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				print("start say...")
				audio = r.listen(source)
				print("speech done..")
				p = r.recognize_google(audio)
				print("you said..  " + p)
				if(("create partition" in p) or ("Create Partition" in p)):
					os.system("fdisk %s"%x)
					os.system("n")
				else:
					print("Dont support.....")


		elif(("hadoop" in p) or ("Hadoop" in p)) or(("hey os can you open hadoop for me" in p)or("Can You Open Hadoop For Me" in p)) or (("open hadoop" in p) or ("run hadoop" in p)) or (("Haadu" in p) or ("haadu" in p)):
			os.chdir('/etc/hadoop')
			os.system("ls")
			print("for cluster, what You want to Make... Namenode or Datanode")
			print("")
			print("")
			os.system("tput setaf 1")
			print("want to make namenode say...namenode")
			print("want to make datanode say...datanode")
			print("")
			t = 3
			for i in range(t):
				print(str(t - i) + "second remain" )
				time.sleep(1)
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				print("start say...")
				audio =  r.listen(source)
				print("speech done")
				p = r.recognize_google(audio)
				print("you said.." + p)
				if(("namenode" in p) or ("Namenode" in p)):
					if os.path.exists('nn'):
						os.rmdir('nn')
						os.mkdir('nn')
						pyttsx3.speak("wait a second directory is removing")
						time.sleep(2)
						print("older namenode directory is removed")
						os.system("tput setaf 6")
						pyttsx3.speak("wait a second new namenode directory is creating for you")
						time.sleep(2)
						pyttsx3.speak("directory is created for you")
						print("new namenode Directory is created")
						time.sleep(5)
						pyttsx3.speak("wait a second we are configuring hdfs-site for you..")
						time.sleep(3)
						print("hdfs-site is configured with new details...")
						pyttsx3.speak("wait a second we are configuring core-site for you..")
						print("wait a second we are configuring core-site for you..")
						time.sleep(3)
						print("core-site is configured with new details...")
						print("wait namenode Formating for the first time...")
						os.system("hadoop namenode -format")
						time.sleep(3)
						keyboard.press_and_release('n, enter')
						print("namenode is successfully formated")
						pyttsx3.speak("nanenode service is starting wait a second")
						print("namenode service is starting wait....")
						time.sleep(3)
						os.system("hadoop-daemon.sh start namenode")
						os.system("jps")
						pyttsx3.speak("Namenode service is started")
						print("namenode service is started")
						system.os("quit")
					elif not os.path.exists('nn'):
						import os
						pyttsx3.speak("wait a second for the first time namenode directory is creating for you")
						time.sleep(2)
						os.mkdir('nn')
						print("new Namenode Directory is Created")
						print("wait a second we Configuring hdfs-site for you")
						time.sleep(3)
						print("hdfs is configured with new details")
					else:
						print("dont support")
						time.sleep(5)
				elif(("datanode" in p) or ("Datanode" in p)) or (("data node" in p) or ("Data Node" in p)):
					if os.path.exists('dn'):
						os.system("tput setaf 9")
						pyttsx3.speak("wait a second we removing previous datanode directory")
						os.rmdir('dn')
						time.sleep(2)
						pyttsx3.speak("directory is removed")
						print("directory is removed")
						pyttsx3.speak("new datanode directory is creating for you")
						print("directory is creating..wait a sec..")
						time.sleep(2)
						os.mkdir('dn')
						pyttsx3.speak("directory is created for you")
						print("directory is created")
					elif not os.path.exists('dn'):
						pyttsx3.speak("wait a second we creating new datanode directory for you")
						print("New datanode Directory is creating for you..")
						time.sleep(2)
						os.mkdir('dn')
						pyttsx3.speak("directroy is created")
						print("new datanode directory is created")
				    else:
					    print("dont support")
		elif(("docker" in p) or ("Docker" in p)) or (("open docker" in p) or ("Open Docker" in p)):
			pyttsx3.speak("wait a second Docker is starting")
			os.system("systemctl start docker")
			time.sleep(2)
			print("docker is running..")
			pyttsx3.speak("docker is running")
			os.system("tput setaf 5")
			pyttsx3.speak("hey user showing all function that you can do in docker")
			os.system("tput setaf 6")
			print("__________these are the function in docker that you can do___________")
			os.system("tput setaf 8")
			print("if you want to download Image:.. say hey OS i want to download Image")
			print("if you want to list running containers...say hey OS i want to list running containers")
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				print("start say...")
				audio = r.listen(source)
				print("speech done...")
				p = r.recognize_google(audio)
				print("you said.." + p)
				pyttsx3.speak("you said %s"%p)
				os.system("tput setaf 3")
				if(("download image" in p) or ("Download Image" in p)) or (("download" in p) or ("Download" in p)):
					pyttsx3.speak("these are the latest available image for download")
					print("\n\n")
					print("__________________Debian__________________")
					print("__________________fedora__________________")
					print("__________________Ubuntu_________________\n\n")
					print("tell me Which OS you want to download\n\n")
					pyttsx3.speak("tell me what do you want to download")
					t = 5
					for i in range(t):
						print(str(t - i) + "second remain" )
						time.sleep(1)
					with sr.Microphone() as source:
						r.adjust_for_ambient_noise(source)
						print("start say...")
						audio = r.listen(source)
						print("speech done...")
						p = r.recognize_google(audio)
						print("you said:" + p)
						pyttsx3.speak("i got it you said : %s"%p)
						if(("debian" in p) or ("Debian" in p)) or (("download debian" in p) or ("Download Debian" in p)):
							pyttsx3.speak("collecting resourses wait..")
							time.sleep(2)
							pyttsx3.speak("downloading wait")
							print("image is downloading wait")
							os.system("docker pull debian")
							pyttsx3.speak("Debian is Successfully downloaded")
							print("download successful..")
						elif(("fedora" in p) or ("Fedora" in p)) or (("download fedora" in p) or ("Download Fedora" in p)):
							pyttsx3.speak("collecting resourses wait..")
							time.sleep(2)
							pyttsx3.speak("downloading wait")
							print("image is downloading wait")
							os.system("docker pull fedora")
							pyttsx3.speak("Fedora is Successfully downloaded")
							print("download successful..")
						elif(("ubuntu" in p) or ("Ubuntu" in p)) or (("download ubuntu" in p) or ("Download Ubuntu" in p)):
                                                	pyttsx3.speak("collecting resourses wait..")
                                                	time.sleep(2)
                                                	pyttsx3.speak("downloading wait")
                                                	print("image is downloading wait")
                                                	os.system("docker pull ubuntu:14.04")
                                                	pyttsx3.speak("Ubuntu is Successfully downloaded")
				elif(("Show Me All Images" in p) or ("show me all images")) or (("All Images" in p) or ("all images" in p)) or (("installed images" in p) or ("Installed Images" in p)):
					pyttsx3.speak("wait a second we listing all Images")
					os.system("docker image ls")
					os.system("tput setaf 1")
					print("\n\n")
					print("do you want to Launch any image if this image is available in this list\n\n")
					print("tell the image name")
					pyttsx3.speak("tell me image name")
					os.system("docker image ls")
					print("\n\n")
					while True:
						with sr.Microphone() as source:
							r.adjust_for_ambient_noise(source)
							print("start say...")
							audio = r.listen(source)
							print("speech done...")
							p = r.recognize_google(audio)
							pyttsx3.speak("i got it you said: %s"%p)
							print("you said: " + p)
							if(("debian" in p) or ("Debian" in p)):
								print("\n\n")
								print("tell me Tag of Image(version)")
								pyttsx3.speak("hey user i want to know Tag of image tell me")
								while True:
									with sr.Microphone() as source:
										r.adjust_for_ambient_noise(source)
										print("start say...")
										audio = r.listen(source)
										print("speech done...")
										p = r.recognize_google(audio)
										pyttsx3.speak("i got it you said: %s" %p)
										print("you said: " + p)
										if(("latest" in p) or ("Latest" in p)):
											pyttsx3.speak("wait i am launing your image")
											time.sleep(2)
											os.system("docker run debian:latest")
											pyttsx3.speak("Debian is running")
											print("\n\n\n")
											os.system("tput setaf 2")
											os.system("docker ps -a")
											pyttsx3.speak("these are the running containers you have")
											pyttsx3.speak("wait you are landing to the bebian terminal..")
											os.system("docker run -it debian:latest")
							elif(("fedora" in p) or ("Fedora" in p)):
								print("\n\n")
								print("tell me Tag Of Image(Version)")
								pyttsx3.speak("hey user i want to know Tag of image.. tell me")
								while True:
									with sr.Microphone() as source:
										r.adjust_for_ambient_noise(source)
										print("start say...")
										audio = r.listen(source)
										print("speech done..")
										p = r.recognize_google(audio)
										pyttsx3.speak("i got it you said: %s" %p)
										print("you said:" + p)
										if(("latest" in p) or ("Latest" in p)):
											pyttsx3.speak("wait i am launching your Image")
											time.sleep(2)
											os.system("docker run fedora:latest")
											pyttsx3.speak("Fedora is Running")
											print("\n\n\n")
											os.system("tput setaf 5")
											os.system("docker ps -a")
											pyttsx3.speak("these are the running containers you have")
											pyttsx3.speak("wait you are landing to the bebian terminal..")
											os.system("docker run -it fedora:latest")
							elif(("ubuntu" in p) or ("Ubuntu" in p)):
								print("\n\n")
								print("tell me Tag Of Image(Version)")
								pyttsx3.speak("hey user i want to know Tag of image.. tell me")
								while True:
									with sr.Microphone() as source:
										r.aadjust_for_ambient_noise(source)
										print("start say..")
										audio = r.listen(source)
										print("speech done..")
										p = r.recognize_google(audio)
										pyttsx3.speak("i got it you said: %s" %p)
										print("you said:" + p)
										if(("latest" in p) or ("Latest" in p)):
											pyttsx3.speak("wait i am launching your image")
											time.sleep(2)
											os.system("docker run ubuntu:14.04")
											pyttsx3.speak("Ubuntu is running")
											print("\n\n\n")
											os.system("tput setaf 9")
											os.system("docker ps -a")
											pyttsx3.speak("these are the running containers you have")
											pyttsx3.speak("wait you are landing to the bebian terminal")
											os.system("docker run -it ubuntu:14.04")
				else:
					print("dont support")
			print("\n\n\n")
		elif(("LVM" in p) or ("lvm" in p)) or (("Logical Volume Management" in p) or ("logical volume management" in p)):
			pyttsx3.speak("Wait a second LVM is starting")
			os.system("tput setaf 1")
			pyttsx3.speak("Showing Available devices")
			print("___You have these Device Available in your OS__")
			print("\n")
			os.system("fdisk -l")
			print("\n\n")
			os.system("tput setaf 8")
			print("__These are the Partition you already have__")
			os.system("lsblk")
			time.sleep(3)
			print("\n")
			pyttsx3.speak("Enter Your Device Names we Creating Physical Volumes and Logical volume For you")
			print("Enter Your First device Name (i.e /dev/sda)")
			x = input("Enter Device : " )
			print("Enter your Second Device name")
			y = input("Enter Device : ")
			os.system("tput setaf 5")
			print("\nYour devices are: %s" %x,y)
			time.sleep(2)
			os.system("zenity --warning")
			os.system("pvcreate %s"%x)
			os.system("pvcreate %s"%y)
			pyttsx3.speak("Physical volume is created")
			print("\nPhysical Volume is Created")
			print("Enter any name for volume group")
			z = input("Enter Name : ")
			os.system("vgcreate {} {} {}".format(z,x,y))
			pyttsx3.speak("Wait a second Logical Volume is groupping for you")
			time.sleep(2)
			pyttsx3.speak("Volume is Grouped")
			pyttsx3.speak("wait i am creating Logical volume please make a directory")
			print("make a Directory")
			d = input("give a path for directory : ")
			os.chdir("%s"%d)
			os.system("pwd")
			print("Give a Name for directroy")
			n = input("Enter Name : ")
			os.mkdir("%s"%n)
			pyttsx3.speak("Directory is created")
			print("Directory is created")
			os.system("cd {}".format(n))
			os.system("tput setaf 3")
			print("Give Size and size should be in K,M,G,T,P Format")
			q = input("Enter Size : ")
			print("Wait a secoud Logical Volume is creating")
			os.system("lvcreate --size {} --name{}".format(q,n))
			pyttsx3.speak("logical volume is created")
			pyttsx3.speak("wait logical volume is formating")
			os.system("mkfs.ext4 {}{}".format(d,n))
			pyttsx3.speak("formated successful")
			os.system("tput setaf 8")
			print("\n\n____________________Final-Step________________\n")
			print("For Mounting this logical volume make a Folder\n")
			print("Enter a path where you want make this folder")
			f = input("Enter path : ")
			os.chdir("%s"%f)
			os.system("pwd")
			print("Enter folder name")
			r = input("Enter name :")
			os.mkdir("%s"%r)
			pyttsx3.speak("wait a second logical Volume is mounting")
			os.system("mount {} {}".format(f,r))
			print("Successfully Mount Your Logical Volume")
			pyttsx3.speak("everything is done")
		else:
			print("dont support")
