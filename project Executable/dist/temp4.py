s = "abc.enc"
sa = "abc.txt"
print(s[-4:])
if ".enc" == s[3: 7]:
	print("Already enc present")
if ".enc" == sa[3: 7]:
	print("Already enc present")
else:
	sa = sa + ".enc"
	print(sa)
