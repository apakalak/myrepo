'''
This file takes a .txt resume file as input and parses it
to collect all the entered data into a dictionary and
print in 'key' : value format
'''

import os

def ParseResume(name):
    """ The method parses the file line by ine and saves all the fields in a dictionary """
    if CheckFileExistence(name):
        with open(name,'r') as resumeFile:
	    dictFields = {}
	    for line in resumeFile:
	        try:
	            line = line.strip(" ")
		    if line:
		        key, value = map(str.strip, line.split(":", 1))
	                dictFields[key] = value.lstrip("\n")
	        except Exception:
                    try:	
                        if key and dictFields.has_key(key):
	                     dictFields[key] += line.lstrip("\n")
                    except UnboundLocalError:
                        pass
	for key in sorted(dictFields.iterkeys()):
	    if dictFields[key] and isMainModule:
	        print "'" + key.upper() + "'    - " + dictFields[key] + "\n"
        return True
    return False


def CheckFileExistence(name):
    """ This method check if the entered resume file exists and is in required format"""
    if not name.endswith(".txt"):
        if isMainModule:
            print "Please enter a valid .txt file!!"
        return False
    elif not os.path.exists(name):
        if isMainModule:
            print os.path.abspath(name) + " does not exist!!"
        return False
    return True

isMainModule = False # This is used to avoid printing of error messages on running the test cases
if __name__ == '__main__':
    isMainModule = True
    name = raw_input("Enter the resume file name with full file path: ")
    name = os.path.abspath(name)
    ParseResume(name)
