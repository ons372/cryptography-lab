import sys
def rot13(string):
	output=""
	for char in string:
		if 'A'<=char<='Z':
			output+=chr((ord(char)-ord('A')+13)%26+ord('A'))
		elif 'a'<=char<='z':
			output+=chr((ord(char)-ord('a')+13)%26+ord('a'))
		else:
			output+=char
	return output
for arg in sys.stdin:
	print(rot13(arg),end="")
