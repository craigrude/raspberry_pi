#fhand = open('sample_text.txt')
#for line in fhand:
	#if line.startswith('From:'):
		#print(line)
#fhand.close()
#print('*'*50)

#fhand = open('sample_text.txt')
#for line in fhand:
	#line = line.rstrip()
	#if line.startswith('From:'):
		#print(line)
#fhand.close()
#print('*'*50)

#fhand = open('sample_text.txt')
#for line in fhand:
	#line = line.rstrip()
	#if not line.startswith('From:'):
		#continue
	#print(line)
#fhand.close()
#print('*'*50)

#fhand = open('sample_text.txt')
#for line in fhand:
	#line = line.rstrip()
	#if not '@uct.ac.za' in line:
		#continue
	#print(line)
#fhand.close()
#print('*'*50)

fname = raw_input('Enter the file name:  ')
fhand = open(fname)
count = 0
for line in fhand:
	if line.startswith('From:'):
		count = count+1
print('There were %i subject lines in %s' % (count,fname))
