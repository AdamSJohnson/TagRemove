import os
import re

ALWAYS_REMOVE = ['[', ']', '(', ')']

def main():
	#Read through our config file
	configFile = open('config.txt') 
	targetRoot = configFile.readline().strip()
	subDirs = configFile.readline().strip().split(',')
	grabPat = configFile.readline().strip()
	pattern = "false"
	if(grabPat != "false"):
		pattern = re.compile(grabPat)
	season = configFile.readline().strip()
	tags = [line.strip() for line in configFile]
	#get the dirs to parse files through
	lookAtTheseDir = ['%s/%s' % (targetRoot, subDir) for subDir in subDirs]
	for dir in lookAtTheseDir:
		for path, subdirs, files in os.walk(dir):
			for file in files:
				fullPath = '%s/%s' % (path, file)
				for tag in tags:
					file = file.replace(tag, '')
				numbers = "false"
				if( pattern != 'false' and season != 'false'):
					numbers = pattern.findall(file)
					s = "{:02}".format( int( season))
					e = "{:02}".format(int(numbers[0]))
					
					file = file.replace(numbers[0], 'S%sE%s' % (s,e )).strip()
				replaceFile =  '%s/%s' % (path, file)
				
				#our always remove list is just ()[] just since they are a pain
				for x in ALWAYS_REMOVE:
					replaceFile = replaceFile.replace(x, '')
				if(numbers != "false" and len(numbers) > 1):
					print("Could not determine episode number")
					print(fullPath)
					print("Modify by hand!!!")
				else:
					print(numbers)
					print(file)
					#os.rename(fullPath, replaceFile)




if __name__ == '__main__':
	main()