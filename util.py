#file to get files, read files, write file
import os.path
import json
def getAllFiles(prefix,path):
	counter=1
	filelist=[]
	while True:
		location = os.path.join(path,prefix+str(counter)+".json")
		if os.path.exists(location) :
			filelist.append(location)
			counter+=1
		else:
			break
	return filelist

def readFile(filepath):
	with open(filepath) as file:
		data = json.load(file)
	return data

def fileWrite(path, filename,jsonstring):
		with open(os.path.join(path,filename), "w") as output_file:
			output_file.write(jsonstring)
