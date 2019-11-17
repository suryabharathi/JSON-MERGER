import json
import os
import util
import copy


def difftodict(integer, dictionary):
	containalphabetflag =False
	numbercontainer=[]
	alphabetconatiner={}
	for key in dictionary:
		if key.isdigit():
			numbercontainer.append(copy.deepcopy(dictionary[key]))
			continue
		else:
			containalphabetflag=True
			alphabetconatiner[key]=copy.deepcopy(dictionary[key])
	if containalphabetflag == False:
		l=[]
		l.append(integer)
		l+numbercontainer
		return l
	else:
		counter=0
		alphabetconatiner[counter]=integer
		counter+=1
		for val in numbercontainer:
			alphabetconatiner[str(counter)]=val
			counter+=1
		return alphabetconatiner


def listdict(lis,dictionary):
	containalphabetflag =False
	numbercontainer=[]
	alphabetconatiner={}
	for key in dictionary:
		if key.isdigit():
			numbercontainer.append(copy.deepcopy(dictionary[key]))
			continue
		else:
			containalphabetflag=True
			alphabetconatiner[key]=copy.deepcopy(dictionary[key])
	if containalphabetflag == False:
		l=[x for x in lis]
		l+numbercontainer
		return l
	else:
		counter=0
		for val in lis:
			alphabetconatiner[counter]=val
			counter+=1
		for val in numbercontainer:
			alphabetconatiner[str(counter)]=val
			counter+=1
		return alphabetconatiner



def json_merge_recursive(json1 , json2):
	for key in json1:
		#print(key , type(json1[key]), type(json2[key]),json1[key],json2[key])
		if json2.get(key) ==None:
			json2[key]=json1.get(key)
        # same type comparison  
		elif type(json1.get(key)) == int and  type(json2.get(key)) == int:
			json2[key]=[json1.get(key),json2.get(key)]

		elif type(json1.get(key))== str and type(json2.get(key))== str:
			json2[key]=[json1.get(key),json2.get(key)]

		elif type(json1.get(key)) == list and type(json2.get(key)) == list:
			l=json1.get(key)
			for val in json2.get(key):
				l.append(val)
			json2[key]=l

		elif type(json1.get(key))==dict and type(json2.get(key))== dict:
			json_merge_recursive(json1.get(key),json2.get(key))

        #int to other type comaparison
		elif (type(json1.get(key)) == int and  type(json2.get(key))==str) or (type(json1.get(key)) == str and  type(json2.get(key))==int):
			json2[key]=[json1.get(key), json2.get(key)]

		elif (type(json1.get(key)) == list and  type(json2.get(key))==int) or (type(json1.get(key)) == int and  type(json2.get(key))==list):
			if type(json1.get(key))==int:
				l=[json1.get(key)]
				l=l+json2.get(key)
			else:
				l=json1.get(key)
				l.append(json2.get(key))
			json2[key]=l

		elif (type(json1.get(key)) == int and  type(json2.get(key))==dict) or (type(json1.get(key)) == dict and  type(json2.get(key))==int):
			if type(json1.get(key)) == int:
				json2[key]=difftodict(json1.get(key),json2.get(key))
			else:
				json2[key]=difftodict(json2.get(key),json1.get(key))


		elif (type(json1.get(key)) == str and  type(json2.get(key))==list) or (type(json1.get(key)) == list and  type(json2.get(key))==str):
			if type(json1.get(key)) == str:
				li=copy.deepcopy(json2[key])
				li.append(json1.get(key))
				json2[key]=li
			else:
				li=copy.deepcopy(json1[key])
				li.append(json2[key])
				json2[key]=li


		elif (type(json1.get(key)) == str and  type(json2.get(key))==dict) or (type(json1.get(key)) == dict and  type(json2.get(key))==str):
			if type(json1.get(key)) == str:
				json2[key]=difftodict(json1.get(key),json2.get(key))
			else:
				json2[key]=difftodict(json2.get(key),json1.get(key))

		elif (type(json1.get(key)) == list and  type(json2.get(key))==dict) or (type(json1.get(key)) == dict and  type(json2.get(key))==list):
			if type(json1.get(key)) == list:
				json2[key]=difftodict(json1.get(key),json2.get(key))
			else:
				json2[key]=difftodict(json2.get(key),json1.get(key))
	return json2


def main():
	path=input("Please Enter the directory Path of your Input Data File: ")
	prefix=input("Please Enter the Prefix of your Input Data File: ")
	size=int(input("Please Enter the max Size of Output File in BYTES: "))
	filepathlist=util.getAllFiles(prefix,path)
	if len(filepathlist)==0:
		mergedjson={}
		raise Exception("The Path entered is either incorrect or the prefix is incorrect  or File Not found")
	elif len(filepathlist)==1:
		mergedjson=util.readFile(filepathlist[0])
	elif len(filepathlist)==2:
		mergedjson=json_merge_recursive(util.readFile(filepathlist[0]),util.readFile(filepathlist[1]))
	else:
		mergedjson=json_merge_recursive(util.readFile(filepathlist[0]),util.readFile(filepathlist[1]))	
		for i in range(2,len(filepathlist)):
			mergedjson=json_merge_recursive(util.readFile(filepathlist[i]),mergedjson)
	jsonstring=json.dumps(mergedjson, indent=2)
	util.fileWrite(path,"merge.json",jsonstring)
	statinfo = os.stat(os.path.join(path,"merge.json"))
	print("merge.json is your output file")
	if statinfo.st_size>size:
		print("The prefered size is slightly more. Can I please minimize the json removing all indentations")
		print("Y/N")
		choice=input()
		if choice =="Y":
			jsonstring=json.dumps(mergedjson)
			util.fileWrite(path,"merge.json",jsonstring)
	statinfo = os.stat(os.path.join(path,"merge.json"))
	if statinfo.st_size>size:
		print("Sorry the file size mentioned is low")
		print("Please try again with more size. Output File Removed")
		os.remove(os.path.join(path,"merge.json"))

if __name__== "__main__":
   main()
