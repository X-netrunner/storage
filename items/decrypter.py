#!/usr/bin/env python3 

import os
from cryptography.fernet import Fernet
from pathlib import Path
import pathlib
#import argparse
import time
from colorama import *

files = []
folders = []
subfolders = []
temp5 = []
#pr_path=[]
pr_temp = False
file_flag=False

def decryption(tempp,key):
	for file in os.listdir():
		if file == "decrypter.py" or file =="thekey.key" or file=="decrypter.py" or file=="test.py":
			continue
		if os.path.isfile(file):
			files.append(file)
	for file in files:
		with open(file, "rb")  as thefile:
			content = thefile.read()
		content_e = Fernet(key).decrypt(content)
		with open(file, "wb") as thefile:
			thefile.write(content_e)
	for temp2 in pathlib.Path(tempp).glob("*"):
		print(Fore.WHITE + "[" + Fore.GREEN  + "*"+ Fore.WHITE + "] decrypting " + Fore.BLUE + f"{temp2}")
	print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] will be skipping few files not fixed yet")

def decrypt(temp_file,key,checker):
	if temp_file == "decrypter.py" or file =="thekey.key" or file=="test.py" or file=="decrypter.py":
		checker=-1
	else :
		with open(temp_file,"rb") as temp3:
			content= temp3.read()
		content_e=Fernet(key).decrypt(content)
		with open(temp_file,"wb") as temp3:
			temp3.write(content_e)
	return checker+1

def decryption_folder(temp1,key):
	for temp2 in pathlib.Path(temp1).glob("*"):
		if temp2.is_file():
			checker=0
			decrypt(temp2 ,key ,checker)
			if checker == 1:
				print(Fore.WHITE + "[" + Fore.GREEN  + "*" +  Fore.WHITE + f"] decrypting {temp2}")
			else :
				print(Fore.WHITE + "[" + Fore.RED + "-"+  Fore.WHITE +f"] decrypting {temp2} ---failed")
		elif temp2.is_dir():
                	decryption_folder(temp2,key)

def decryptionfilename(name):
	temp_data=[]
#	print("passed")
	for file in os.listdir():
		if os.path.isfile(file):
			temp_data.append(file)
		elif os.path.isdir(file):
			temp_data.append(file)
#	print(temp_data)
	root=Path.cwd()
	checker=0
	for file in os.listdir():
		if checker <=len(temp_data) and checker != -1:
#			print(name,temp_data[checker])
			if name == temp_data[checker]:
#				print("passed")
				final = os.path.join(root, name)
				print (Fore.WHITE + "[" + Fore.GREEN + "*" +Fore.WHITE +"] Path location : " + Fore.BLUE + final)
				with open(name, "rb")  as thefile:
					content = thefile.read()
				content_e = Fernet(key).decrypt(content)
				with open(name, "wb") as thefile:
					thefile.write(content_e)
				print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE + "] decrypting " + Fore.BLUE + f"{final}")
				checker=-1
			else :
#check to split the .txt etc names and find out the filepattern
				checker=checker+1
		else:
			break
	
def dir_file():
	time.sleep(1)
	temp_data=[]
	for file in os.listdir():
		if os.path.isfile(file):
			temp_data.append(file)
		elif os.path.isdir(file):
			temp_data.append(file)
	print(Fore.CYAN , temp_data)
	
def chdr(temp_dir = None ):
	if pr_temp == True :
#		print("True",pr_path[0],temp_dir)
#		temp_sf = str(pr_path[0])
		t_bin3 = str(Path.cwd()).split("/")
		t_bin2 = len(t_bin3) - 1
		t_bin1 = t_bin3.pop(t_bin2)
		temp_sf = "/".join(t_bin3)
		
	else : 
#		print("False")
		root=Path.cwd()
		temp_sf=str(root)+"/"+str(temp_dir)
	print(temp_sf)
	os.chdir(temp_sf)

def totalno_subfolders():
	for root,dirs,files in os.walk(Path.cwd()):
			for temp4 in dirs:
				temp5.append(temp4)
	print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE +"] Total number of subfolders which will be decrypted :" + str(len(temp5)))

def incorrect():
	print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + " password is wrong \n" + Fore.WHITE + "[" + Fore.YELLOW + "[!] Ending task")
	time.sleep(0.5)
	print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE + "] done")
	exit()

def s_lit(t_syn):
	i=0
	bin_syn1=t_syn.split()
	if file_flag == True :
		bin_syn2=bin_syn1.pop(1)
		bin_syn3=bin_syn2.split(".")
		for i in range(2):
			bin_syn1.append(str(bin_syn2[i]))
			++i
	else : 
		print(bin_syn1)
		return bin_syn1

print(Fore.WHITE + "\t \t \t D.E.C.R.Y.P.T.E.R")
print(Fore.WHITE + "-------------------------------------------------------------------------")
print(Fore.YELLOW + "few  options : \n 1.decrypt all files in the location \n 2.decrypt all files inside folders avaliable as well \n 3.decrypt a specific file ")
option = input("selection :")
print(Fore.WHITE + "[" + Fore.GREEN  + "*"+  Fore.WHITE +"] Working on it...\n" + Fore.WHITE + "[" + Fore.GREEN +"*" + Fore.WHITE + "] decrypting...")


subfolders = [f.path for f in os.scandir(Path.cwd()) if f.is_dir()]
subfolders_no=len(subfolders)
checker=0


password = input(Fore.YELLOW + "enter password:"+ Fore.RED + "")
print(Fore.WHITE + "-------------------------------------------------------------------------")
key_checker=0
if password =="retsu":
	time.sleep(1)
	for file in os.listdir():
		if file == "thekey.key":
			print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE  + "] key already found.. \n" + Fore.WHITE + "[" + Fore.GREEN +"*" +Fore.WHITE + "] aborting key creation")
			time.sleep(1)
			print(Fore.WHITE + "[" + Fore.GREEN  + "*" +  Fore.WHITE + "] done...")
			print(Fore.WHITE + "[" + Fore.GREEN  + "*" +  Fore.WHITE + "] Using found key")
			print(Fore.WHITE + "-------------------------------------------------------------------------")
			key_checker=0
			break
		else :
			key_checker=1
else:
	incorrect()
if key_checker == 1:
		key = Fernet.generate_key()
		print(Fore.WHITE + "[" + Fore.RED + "-" +  Fore.WHITE + "] no exisiting key was found \n" + Fore.WHITE + "[" + Fore.GREEN + "*" + Fore.WHITE + "] Making new key")
		with open("thekey.key","wb") as thekey:
			thekey.write(key)
		print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE + "] succesful,key made")
		print(Fore.WHITE + "-------------------------------------------------------------------------")
else :
	temp_key = open("thekey.key", mode="rb")
	key=temp_key.read()

if option == "1":
	tempp=Path.cwd()
	decryption(tempp,key)
	
elif option == "2" :
	for folder in os.listdir():
		if os.path.isdir(folder):
			folders.append(folder)
	totalno_subfolders()
	for temp_sub in range(subfolders_no):
		temp_path=subfolders[temp_sub]
		if os.path.isdir(temp_path):
			decryption(temp_path,key)
			decryption_folder(temp_path,key)
		elif os.path.isfile(temp_path):
			decryption(temp_path,key)
		
elif option =="3" :
	temp_list=[]
#	pr_folder=[]
	dir_file()
	print("")
	print(Fore.WHITE + "-------------------------------------------------------------------------")
	print(Fore.WHITE + "[" +Fore.YELLOW  + "!" +  Fore.WHITE + "] Follow the synatx : \n\t"+ Fore.WHITE + "1.If its a folder, " + Fore.YELLOW + "syntax: folder <foldername> \n\t"+ Fore.WHITE + "2.If its a file, " + Fore.YELLOW + "syntax: file <filename>")
	temp_syn=input(Fore.WHITE + "[" + Fore.YELLOW  + "!" + Fore.WHITE + "] Enter syntax:" + Fore.RED + "")
	temp_list2 = s_lit(temp_syn)
	temp_list=temp_syn.split()
#	pr_folder.append(temp_list[1])
#	pr_path.append(Path.cwd())
#	print("dignostics=--------=")
#	print(temp_syn.split())
#	print(temp_list[0])
	if temp_list[0] == "folder":
		for i in range(-10,10):
			bin_list = []
			if len(temp_list) >=2:
#				print(temp_list[0])
				chdr(temp_list[1])
				del temp_list[1]
			dir_file()
			print(Fore.WHITE + "[" + Fore.YELLOW  + "*"+ Fore.WHITE + "] Follow the synatx : \n\t" + Fore.WHITE + "1.If its a folder, " + Fore.YELLOW + "syntax: folder <foldername> \n\t" + Fore.WHITE + "2.If its a file, " + Fore.YELLOW + "syntax: file <filename.filetype> \n\t" + Fore.WHITE + "3.To refresh files in folder, " + Fore.YELLOW + "syntax: refresh \n\t" + Fore.WHITE + "4.To go back, " + Fore.YELLOW + "syntax: back" )
			bin_syn=input(Fore.WHITE + "[" + Fore.YELLOW  + "!" + Fore.WHITE + "] Enter syntax: " + Fore.RED + "")
			bin_list=bin_syn.split()
			bin_list2 = s_lit(bin_syn)
			if bin_list[0] == "folder":
#				print(pr_path,pr_folder)
#				del pr_path[0]
#				del pr_folder[0]
#				pr_folder.append(bin_list[1])
#				pr_path.append(Path.cwd())
				i=5
				temp_list.append(bin_list[1])
				continue
			elif bin_list[0] =="file":
				i=i+100
				file_flag=True
				print(temp_list2)
				decryptionfilename(bin_list[1])
				print(Fore.WHITE + "[" + Fore.YELLOW+ "!" + Fore.WHITE + "] Deleting waste..")
				del bin_list
				print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE + "] completed")
				break
			elif bin_list[0] == "refresh":
				print(Fore.YELLOW + "[!] folder path ...",Path.cwd())
				dir_file()
				i=-5
				print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE + "] Refresh completed")
			elif bin_list[0] == "back":
				pr_temp = True 
				print(Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "] Going back ")
#				chdr(pr_folder[0])
				chdr()
				print(Fore.WHITE + "[" + Fore.GREEN + "*" + Fore.WHITE + "] Done")
#				del pr_path[0]
#				del pr_folder[0]
				i=-5
				pr_temp = False
			else:
				print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] error:Couldn't recognise syntax")
	elif temp_list[0]== "file":
#		print("correct")
#		time.sleep(10)
		print(temp_list2)
		decryptionfilename(temp_list[1])
	else :
		print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE +" error:Couldn't recognise syntax ")
		
		
		
