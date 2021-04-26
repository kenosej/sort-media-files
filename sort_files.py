import os
import magic
from datetime import datetime

srcPath = "putPathHere"
outputPath = "putPathHere"

def makeIfNotExists(path):
	if not os.path.exists(path):
		os.mkdir(path)

def make1stPaths(dateName):
	path = outputPath + "/" + dateName[-4:]
	makeIfNotExists(path)

def make2ndPaths(dateName):
	path = outputPath + "/" + dateName[-4:] + "/" + dateName
	makeIfNotExists(path)

def make3rdPaths(dateName, fullName):
	path = outputPath + "/" + dateName[-4:] + "/" + dateName + "/" + adaptExt(recognizeFileType(fullName))
	makeIfNotExists(path)
	return path

def adaptExt(mime):
	if mime != "image" and mime != "video" and mime != "audio":
		return "other"
	return mime

def recognizeFileType(fullName):
	return magic.from_file(fullName, mime=True)[:5]

def copyToSorted(fullName, name, outputPath):
	command = "cp -p '" + fullName + "' '" + outputPath + "/" + name + "'"
	print("Executing:", command)
	os.popen(command)

def traverse():
	for root, dirs, files in os.walk(srcPath):
		for name in files:
			fullName = os.path.join(root, name)
			dateName = datetime.utcfromtimestamp(os.path.getmtime(fullName)).strftime("%m-%Y")

			recognizeFileType(fullName)
			make1stPaths(dateName)
			make2ndPaths(dateName)
			copyToSorted(fullName, name, make3rdPaths(dateName, fullName))

traverse()

