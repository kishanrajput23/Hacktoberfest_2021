# Python 3 program to find lexicographically
# next string

def nextWord(s):
	
	# If string is empty.
	if (s == " "):
		return "a"

	# Find first character from right
	# which is not z.
	i = len(s) - 1
	while (s[i] == 'z' and i >= 0):
		i -= 1

	# If all characters are 'z', append
	# an 'a' at the end.
	if (i == -1):
		s = s + 'a'

	# If there are some non-z characters
	else:
		s = s.replace(s[i], chr(ord(s[i]) + 1), 1)

	return s

# Driver code
if __name__ == '__main__':
	str = "samez"
	print(nextWord(str))
	
# This code is contributed by
# Sanjit_Prasad
