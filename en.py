import marshal

file = input("File --> : ")
Open_Raed = open(file).read()
Compel = compile(Open_Raed, '', 'exec')
Dumps = marshal.dumps(Compel)
Start = open('en_' + file, 'w')
Start.write('#Coded By Aspitgans Yah Kali Lu bisa dec ni\nimport marshal\n')
Start.write('exec(marshal.loads(' + repr(Dumps) + '))')
Start.close()
print(' Done')
