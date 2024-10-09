import sys
def rotN(string,count=13):
	output=""
	for char in string:
		if 'A'<=char<='Z':
			output+=chr((ord(char)-ord('A')+count)%26+ord('A'))
		elif 'a'<=char<='z':
			output+=chr((ord(char)-ord('a')+count)%26+ord('a'))
		else:
			output+=char
	return output

if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("error")
            sys.exit(1)
else:
	count = 13
for arg in sys.stdin:
	print(rotN(arg,count),end="")
