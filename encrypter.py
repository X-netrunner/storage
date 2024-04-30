#!/usr/bin/env python3 

import os
from cryptography.fernet import *
from pathlib import Path
import pathlib
#import argparse
import time
from colorama import *
import shutil
from datetime import *


global log_data , dir_path  , dev_input
t_file = None
log_data = []
files = []
folders = []
subfolders = []
temp5 = []
dir_path=Path.cwd()
pr_temp = False
file_flag=False
op=True
dev_input = False



def log(o_path):
	global log_option 
	log_option = False
	chdr("e_folder",o_path)
	print(Path.cwd())
	log_option = os.path.exists(str(Path.cwd()) + "/log.txt")
	print(log_option)
	if log_option == True :
		print("passed thou 1st option")
		shutil.move(str(Path.cwd()) + "/log.txt",str(o_path))
		log_writer(log_option)
	else :
		print("not detected")
		beta_f_name = str(o_path) + "/log.txt"
		aplha_f_name=s_error_fix(beta_f_name)
		t_file = open(aplha_f_name, "w")
		t_file.close()
		log_writer(log_option)
		
def log_writer(log_option):
	beta_f_name = str(dir_path) + "/log.txt"
	aplha_f_name=s_error_fix(beta_f_name)
	log_file = open(aplha_f_name, "a")
	if (log_option == True ):
		log_file.write("\n\nNew Log --" + str(datetime.now()) + "\n")
		for n in range(len(log_data)):
			log_file.write("\t" + str(datetime.now()) + "||" + str(log_data[n]) + "\n")
			n=n+1
	else:
		log_file.write( "\t\t\t\t\t\t LOG FILE FOR ENCRYPTER--\t\t Date:" + str(date.today()) + "\n")
		log_file.write("\n\nNew Log --" + str(datetime.now()) + "\n")
		for n in range(len(log_data)):
			log_file.write("\t" + str(datetime.now()) + "||" + str(log_data[n]) + "\n")
	shutil.move(str(dir_path) + "/" + "log.txt",str(dir_path) + "/" + "e_folder")
	log_file.close()

def s_error_fix(x):
	y=[]
	y=x.split("/")
	z="//".join(y)
	log_data.append("--// fix for windows for path : " + z)
	return z

def encryption(tempp,key,root_req):
	for file in os.listdir():
		if file == "encrypter.py" or file =="e_key.key" or file=="decrypter.py" or file=="test.py":
			continue
		if os.path.isfile(file):
			files.append(file)
	if root_req == False :
		global count
		count = 0
		for file in files:
			with open(file, "rb")  as thefile:
				content = thefile.read()
			content_e = Fernet(key).encrypt(content)
			with open(file, "wb") as thefile:
				thefile.write(content_e)
		for temp2 in pathlib.Path(tempp).glob("*"):
			print(Fore.WHITE + "[" + Fore.GREEN  + "*"+ Fore.WHITE + "] Encrypting " + Fore.BLUE + f"{temp2}")
			log.append("Encrypted file path : " + str(temp2))
			count = count+1
		log.append("Number of files encrypted : " + str(count))
		print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] will be skipping few files not fixed yet")
	else :
		log.appennd("Debugging reply : No error found")
		
def encrypt(temp_file,key,checker):
	if temp_file == "encrypter.py" or file =="e_key.key" or file=="test.py" or file=="decrypter.py":
		checker=-1
	else :
		with open(temp_file,"rb") as temp3:
			content= temp3.read()
		content_e=Fernet(key).encrypt(content)
		with open(temp_file,"wb") as temp3:
			temp3.write(content_e)
	return checker+1

def encryption_folder(temp1,key):
	for temp2 in pathlib.Path(temp1).glob("*"):
		if temp2.is_file():
			checker=0
			encrypt(temp2 ,key ,checker)
			if checker == 1:
				print(Fore.WHITE + "[" + Fore.GREEN  + "*" +  Fore.WHITE + f"] Encrypting {temp2}")
			else :
				print(Fore.WHITE + "[" + Fore.RED + "-"+  Fore.WHITE +f"] Encrypting {temp2} ---failed")
		elif temp2.is_dir():
                	encryption_folder(temp2,key)

def encryptionfilename(name):
	temp_data=[]
	for file in os.listdir():
		if os.path.isfile(file):
			temp_data.append(file)
		elif os.path.isdir(file):
			temp_data.append(file)
	root=Path.cwd()
	checker=0
	for file in os.listdir():
		if checker <=len(temp_data) and checker != -1:
			if name == temp_data[checker]:
				final = os.path.join(root, name)
				print (Fore.WHITE + "[" + Fore.GREEN + "*" +Fore.WHITE +"] Path location : " + Fore.BLUE + final)
				with open(name, "rb")  as thefile:
					content = thefile.read()
				content_e = Fernet(key).encrypt(content)
				with open(name, "wb") as thefile:
					thefile.write(content_e)
				print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE + "] Encrypting " + Fore.BLUE + f"{final}")
				log_data.append("Encrypted file path : " + str(final))
				log_data.append("Number of encrypted files : 1")
				checker=-1
			else :
#check to split the .txt etc names and find out the filepattern
				checker=checker+1
		else:
			break
	
def dir_file():
	temp_dfile=[]
	temp_dfolder=[]
	for file in os.listdir():
		if os.path.isfile(file):
			temp_dfile.append(file)
		elif os.path.isdir(file):
			temp_dfolder.append(file)
	print(Fore.CYAN +"Files : "+ str(temp_dfile)+ "\nFolders : " + str(temp_dfolder))
	
def chdr(temp_dir = None,additional_path=None):
	if pr_temp == True:
		t_bin3 = str(Path.cwd()).split("/")
		t_bin2 = len(t_bin3) - 1
		t_bin1 = t_bin3.pop(t_bin2)
		beta_temp_sf = "/".join(t_bin3)
		temp_sf = s_error_fix(beta_temp_sf)
		
	else : 
		if additional_path !=None :
			root=additional_path
		else :
			root = Path.cwd()
		beta_temp_sf=str(root)+"/"+str(temp_dir + "/")
		temp_sf = s_error_fix(beta_temp_sf)
	log_data.append("Dir changed to : " + temp_sf)
	os.chdir(temp_sf)

def totalno_subfolders():
	for root,dirs,files in os.walk(Path.cwd()):
			for temp4 in dirs:
				temp5.append(temp4)
	print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE +"] Total number of subfolders which will be encrypted :" + str(len(temp5)))
	log_data.append("Total number of subfolders found :" + str(len(temp5)))

def incorrect(error_line = None , error_type = None):
	if error_line == 223:
		print(Fore.RED + "[-] password is wrong \n"  + Fore.YELLOW + "[!] Ending task")
		print(Fore.GREEN  +"[*] done")
	log_data.append(error_type + " Error : line " + str(error_line) + " --> line 180	")
	log(dir_path)
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

def mdir(temp_file,temp_folder,temp_op,o_path):
	if temp_op == True :
		log_data.append("Key location : Not in encry_f folder ----> moved to secondary location")
		shutil.move(str(o_path) + "/" + "e_key.key",str(o_path) + "/" + "encry_f")
	if temp_op == False :
		log_data.append("Key location : In folder ----> moved to primary location")
		shutil.move(str(o_path) + "/" +"encry_f" + "/e_key.key",str(o_path) + "/")

print(Fore.WHITE + "\t \t \t E.N.C.R.Y.P.T.E.R")
print(Fore.WHITE + "-------------------------------------------------------------------------")
print(Fore.YELLOW + "few  options : \n 1.Encrypt all files in the location \n 2.Encrypt all files inside folders avaliable as well \n 3.Encrypt a specific file ")
option = input("selection :")
print(Fore.WHITE + "[" + Fore.YELLOW  + "!"+  Fore.BLUE +"] Requesting Credentials\n" + Fore.WHITE + "[" + Fore.GREEN +"*" + Fore.WHITE + "] Sent data")


subfolders = [f.path for f in os.scandir(Path.cwd()) if f.is_dir()]
subfolders_no=len(subfolders)
checker=0

user_name = input(Fore.YELLOW + "enter username:" + Fore.RED +" ")
password = input(Fore.YELLOW + "enter password:"+ Fore.RED + " ")
print(Fore.WHITE + "-------------------------------------------------------------------------")
key_checker=0

#option to force  make a  new key
if password =="netrunner" or password == "root" or password == "kali":
	k_check = os.path.exists(str(Path.cwd()) + "/e_folder/e_key.key")
	if k_check == True:
		print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE  + "] key already found.. \n" + Fore.WHITE + "[" + Fore.GREEN +"*" +Fore.WHITE + "] aborting key creation")
		print(Fore.WHITE + "[" + Fore.GREEN  + "*" +  Fore.WHITE + "] done...")
		print(Fore.WHITE + "[" + Fore.GREEN  + "*" +  Fore.WHITE + "] Using found key")
		print(Fore.WHITE + "-------------------------------------------------------------------------")
		key_checker=0
	else :
		print(Path.cwd())
		print(k_check)
		key_checker=1
else:
	log_data.append("Username used : " +user_name )
	log_data.append("Password used : " +password )
	log_data.append("Main option selected : " + option)
	incorrect(242,"Password")

#giving data into the log_data list
log_data.append("Username used : " +user_name )
log_data.append("Password used : " +password )
log_data.append("Main option selected : " + option)

if user_name == "root" and password == "root":
	log_data.append("Developer mode : Active")
	root_input=input(Fore.YELLOW + "[!] Developer option , do you wish to run this program in debugging mode ? : \n Option (Y/N):")
	if root_input == "y" or root_input == "Y":
		dev_input = True
		log_data.append("Debugging mode : Active ")
	else : 
		dev_input = False
		print(Fore.BLUE + "Going though the program normally")
		log_data.append("Debugging option : Deactive")
else :
	log_data.append("Developer mode :Deactive")
	
	
if "e_folder" in os.listdir():
	log_data.append("folder creation : Already present")
	op = False
	mdir("e_key.key","e_folder",op,dir_path)
		

if key_checker == 1:
		key = Fernet.generate_key()
		print(Fore.WHITE + "[" + Fore.RED + "-" +  Fore.WHITE + "] no exisiting key was found \n" + Fore.WHITE + "[" + Fore.GREEN + "*" + Fore.WHITE + "] Making new key")
		with open("e_key.key","wb") as e_key:
			e_key.write(key)
		print(Fore.WHITE + "[" + Fore.GREEN  + "*" + Fore.WHITE + "] succesful,key made")
		print(Fore.WHITE + "-------------------------------------------------------------------------")
		log_data.append("Key status : New key created")
		log_data.append("Key : " + str(key) )
else :
	temp_key = open("e_key.key", mode="rb")
	key=temp_key.read()
	log_data.append("Key status : Exisiting key was found ")
	log_data.append("Key : " + str(key))

if option == "1":
	tempp=Path.cwd()
	encryption(tempp,key,dev_input)
	log.append("Error : None ")
	
elif option == "2" :
	#	fix it
	log.append("2nd option is not working please fix it later")
	for folder in os.listdir():
		if os.path.isdir(folder):
			folders.append(folder)
	totalno_subfolders()
	for temp_sub in range(subfolders_no):
		temp_path=subfolders[temp_sub]
		if os.path.isdir(temp_path):
			encryption(temp_path,key)
			encryption_folder(temp_path,key)
		elif os.path.isfile(temp_path):
			encryption(temp_path,key)
		
elif option =="3" :
	global t_count
	t_count = 1
	if dev_input == False :
		temp_list=[]
		dir_file()
		print(Fore.WHITE + "-------------------------------------------------------------------------")
		print(Fore.WHITE + "[" +Fore.YELLOW  + "!" +  Fore.WHITE + "] Follow the synatx : \n\t"+ Fore.WHITE + "1.If its a folder, " + Fore.YELLOW + "syntax: folder <foldername> \n\t"+ Fore.WHITE + "2.If its a file, " + Fore.YELLOW + "syntax: file <filename>")
		temp_syn=input(Fore.WHITE + "[" + Fore.YELLOW  + "!" + Fore.WHITE + "] Enter syntax:" + Fore.RED + "")
		log_data.append(str(t_count) + "st choice : "  + temp_syn)
		temp_list2 = s_lit(temp_syn)
		temp_list=temp_syn.split()
		if temp_list[0] == "folder":
			for i in range(-10,10):
				bin_list = []
				if len(temp_list) >=2:
					chdr(temp_list[1])
					del temp_list[1]
				dir_file()
				print(Fore.WHITE + "[" + Fore.YELLOW  + "*"+ Fore.WHITE + "] Follow the synatx : \n\t" + Fore.WHITE + "1.If its a folder, " + Fore.YELLOW + "syntax: folder <foldername> \n\t" + Fore.WHITE + "2.If its a file, " + Fore.YELLOW + "syntax: file <filename.filetype> \n\t" + Fore.WHITE + "3.To refresh files in folder, " + Fore.YELLOW + "syntax: refresh \n\t" + Fore.WHITE + "4.To go back, " + Fore.YELLOW + "syntax: back" )
				bin_syn=input(Fore.WHITE + "[" + Fore.YELLOW  + "!" + Fore.WHITE + "] Enter syntax: " + Fore.RED + "")
				bin_list=bin_syn.split()
				t_count = t_count +1
				if t_count == 2 :
					log_data.append(str(t_count) + "nd choice : " + bin_syn)
				elif t_count == 3  :
					log_data.append(str(t_count) + "rd choice : " + bin_syn)
				else :
					log_data.append(str(t_count) + "th choice : " + bin_syn)
				bin_list2 = s_lit(bin_syn)
				if bin_list[0] == "folder":
					i=5
					temp_list.append(bin_list[1])
					continue
				elif bin_list[0] =="file":
					i=i+100
					file_flag=True
					print(temp_list2)
					encryptionfilename(bin_list[1])
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
					chdr()
					print(Fore.WHITE + "[" + Fore.GREEN + "*" + Fore.WHITE + "] Done")
					i=-5
					pr_temp = False
				else:
					print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "] error:Couldn't recognise syntax")
					incorrect(320 , "invalid option ")
		elif temp_list[0]== "file":
			print(temp_list2)
			encryptionfilename(temp_list[1])
		else :
			mdir("e_key.key","e_folder",True,dir_path)
			print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE +" error:Couldn't recognise syntax ")
			incorrect(308 , "invalid option ")
	else : 
		log_data.append("Debuggiing reply : No error found")

if op == True :
	os.mkdir(str(dir_path) + "/encry_f")
	log_data.append("Folder creation :  New folder created")
mdir("e_key.key","e_folder", True , dir_path)

log(dir_path)


