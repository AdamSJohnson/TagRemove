import os
import re

ALWAYS_REMOVE = ['[', ']', '(', ')']
DIRNAME = os.path.dirname(__file__)


if os.name == 'nt':
    SLASH = '\\'

def main():
    print(DIRNAME)
    #Read through our config file
    configFile = open('config.txt') 
    targetRoot = configFile.readline().strip()
    subDirs = configFile.readline().strip().split(',')
    grabPat = configFile.readline().strip()
    pattern = "false"
    if(grabPat != "false"):
        pattern = re.compile(grabPat)
    season = configFile.readline().strip()
    regTag = configFile.readline().strip()
    regTag = re.compile(regTag)
    tags = [line.strip() for line in configFile]
    #get the dirs to parse files through
    lookAtTheseDir = ['%s%s%s' % (targetRoot,SLASH, subDir) for subDir in subDirs]
    for dir in lookAtTheseDir:
        for path, subdirs, files in os.walk(dir):
            for file in files:
                fullPath = '%s%s%s' % (path,SLASH, file)
                matchedRegTags = regTag.findall(file)
                for matchedRegTag in matchedRegTags:
                    file = file.replace(matchedRegTag, '')
                
                for tag in tags:
                    file = file.replace(tag, '')
                print(file)
                #our always remove list is just ()[] just since they are a pain
                for x in ALWAYS_REMOVE:
                    file = file.replace(x, '')
                print(file)
                #Because some extensions have numbers in them the file will be split
                #here and then rebuilt
                splittyThing = file.split('.')
                
                extension = splittyThing.pop()
                fileWithoutExtension = '.'.join(splittyThing)

                numbers = "false"
                if( pattern != 'false' and season != 'false'):
                    print(fileWithoutExtension)
                    numbers = pattern.findall(fileWithoutExtension)
                    s = "{:02}".format( int( season))
                    e = "{:02}".format(int(numbers[0]))
                    
                    fileWithoutExtension = fileWithoutExtension.replace(numbers[0], 'S%sE%s' % (s,e )).strip()
                #recombine the file and extension with extra trailing spaces trimmed
                file = '%s.%s' % (fileWithoutExtension.strip(),extension)

                replaceFile =  '%s%s%s' % (path,SLASH, file)
                
                
                
                
                if(numbers != "false" and len(numbers) > 1):
                    print("Could not determine episode number")
                    print(fullPath)
                    print(replaceFile)
                    print(numbers)
                    print("Modify by hand!!!")
                else:
                    os.rename(fullPath, replaceFile)




if __name__ == '__main__':
    main()