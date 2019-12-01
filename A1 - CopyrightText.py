## A1) Add the copyright text for all the files in a folder. Sample: Copyright © 2019 DSU. All Rights Reserved.
        
# Limitations: Only folders in current directory--or at least that's what happened while testing.
def add_copyright_text(mypath):
	from os import listdir
	from os.path import isfile, isdir, join
	
	if not isdir(mypath):
		print("There is no such folder.")
		return
		
	onlyfiles = [join(mypath, i) for i in listdir(mypath) if isfile(join(mypath, i))]
	print(onlyfiles)

	for i in onlyfiles:
		try:
			cur = open(i, 'at')
			cur.write("\nCopyright © 2019 DSU")
			cur.close()
		except: print("Unable to append to {}".format(i))
		
if __name__ == '__main__':
	mypath = input()
	add_copyright_text(mypath)
        
