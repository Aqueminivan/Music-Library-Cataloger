import os
musicFile = open('music.txt', 'w')

for dirname, dirnames, filenames in os.walk('/home/levi/Music'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        musicFile.write(os.path.join(dirname, subdirname + '\n'))
	#print(os.path.join(dirname, subdirname))
    # print path to all filenames.
    #for filename in filenames:
        #print(os.path.join(dirname, filename))
musicFile.close()
